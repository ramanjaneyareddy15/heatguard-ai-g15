#!/usr/bin/env python3
"""HeatGuard AI v2.0.0 offline prototype. Advisory generation is rule-based mock output."""
import argparse, json, os, re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import heatguard as hg

APP_VERSION = "2.0.0"
ROOT = Path(__file__).resolve().parent
STATIC = ROOT / "static"
AUDIENCES = ["general public", "students", "campus staff", "community communication team"]
SECTIONS = ["advisory headline", "main message", "practical general precautions", "missing/uncertain information"]
MAX_BODY = 100_000

def build_case(data):
    forecast = str(data.get("forecast_text", "")).strip()
    if not forecast:
        raise ValueError("Forecast text is required.")
    audience = str(data.get("audience", "general public")).strip().lower()
    if audience not in AUDIENCES:
        raise ValueError("Unknown audience.")
    try:
        max_words = int(data.get("max_words", 120))
    except (TypeError, ValueError):
        raise ValueError("Maximum words must be a number.")
    if not 20 <= max_words <= 500:
        raise ValueError("Maximum words must be between 20 and 500.")
    def opt(key):
        value = data.get(key)
        value = str(value).strip() if value is not None else ""
        return value or None
    return {"id":"custom","label":"Custom input","forecast_text":forecast,
        "location":opt("location"),"period":opt("period"),"warning_level":opt("warning_level"),
        "audience":audience,"language":str(data.get("language") or "English").strip(),
        "max_words":max_words}

def review_output(case, text):
    supplied = " ".join(filter(None,[case["forecast_text"],case.get("location"),case.get("period"),case.get("warning_level")]))
    supplied_numbers = set(re.findall(r"\d+(?:\.\d+)?", supplied))
    body_lines = [ln for ln in text.splitlines() if not re.match(r"^\s*\d\.\s", ln)]
    output_numbers = re.findall(r"\d+(?:\.\d+)?", "\n".join(body_lines))
    unsupported = sorted({n for n in output_numbers if n not in supplied_numbers})
    lowered = text.lower()
    missing_sections = [s for s in SECTIONS if s not in lowered]
    words = len(text.split())
    findings = []
    if unsupported:
        findings.append({"level":"warn","text":"Numbers in the output that are not in the supplied data: "+", ".join(unsupported)})
    else:
        findings.append({"level":"ok","text":"No numbers found that are missing from the supplied data."})
    findings.append({"level":"warn" if missing_sections else "ok",
        "text":("Missing section(s): "+", ".join(missing_sections)) if missing_sections else "All four required sections are present."})
    findings.append({"level":"warn" if words > case["max_words"] else "ok",
        "text":f"Word count: {words}; limit: {case['max_words']}."})
    findings.append({"level":"ok" if "official" in lowered else "warn",
        "text":"Mentions official guidance." if "official" in lowered else "No pointer to official local guidance found."})
    unset=[k for k in ("location","period","warning_level") if not case.get(k)]
    if unset and not any(w in lowered for w in ("not provided","was not","missing","unknown")):
        findings.append({"level":"warn","text":"Input fields were missing ("+", ".join(unset)+") but the output does not say so."})
    return {"words":words,"findings":findings,
        "note":"Automatic checks are limited and are not semantic hallucination detection. A person must review the draft."}

class Handler(BaseHTTPRequestHandler):
    def _send(self,status,body,content_type="application/json; charset=utf-8"):
        if not isinstance(body,bytes): body=json.dumps(body,ensure_ascii=False).encode("utf-8")
        self.send_response(status); self.send_header("Content-Type",content_type)
        self.send_header("Content-Length",str(len(body))); self.send_header("Cache-Control","no-store")
        self.end_headers(); self.wfile.write(body)
    def do_GET(self):
        path=self.path.split("?")[0]
        if path=="/health":
            return self._send(200,{"status":"ok","service":"heatguard-ai-g15","version":APP_VERSION})
        if path=="/api/version":
            return self._send(200,{"name":"HeatGuard AI","version":APP_VERSION,
                "generation_mode":"rule_based_mock","model_connected":False,"weather_api_connected":False})
        if path=="/api/cases": return self._send(200,{"cases":hg.load_cases(),"audiences":AUDIENCES})
        if path in ("/","/index.html"): return self._send(200,(STATIC/"index.html").read_bytes(),"text/html; charset=utf-8")
        self._send(404,{"error":"Not found"})
    def do_POST(self):
        path=self.path.split("?")[0]
        try:
            length=int(self.headers.get("Content-Length",0))
            if length>MAX_BODY: return self._send(413,{"error":"Request too large."})
            data=json.loads(self.rfile.read(length) or b"{}")
            if not isinstance(data,dict): raise ValueError("Request body must be a JSON object.")
            if path=="/api/generate":
                version=data.get("prompt_version","baseline")
                if version not in ("baseline","structured"): raise ValueError("Unknown prompt version.")
                case=build_case(data); prompt=hg.fill_prompt(hg.load_template(version),case)
                mock=hg.mock_output(case).split("\n\n[mock",1)[0]
                return self._send(200,{"prompt":prompt,"output":mock,"is_mock":True,"review":review_output(case,mock),"version":APP_VERSION})
            if path=="/api/review":
                case=build_case(data); output=str(data.get("output_text","")).strip()
                if not output: raise ValueError("Paste the output text to review.")
                return self._send(200,{"review":review_output(case,output),"version":APP_VERSION})
            self._send(404,{"error":"Not found"})
        except (ValueError,json.JSONDecodeError) as e: self._send(400,{"error":str(e)})
        except Exception: self._send(500,{"error":"Server error."})
    def log_message(self,fmt,*args): print("[%s] %s"%(self.log_date_time_string(),fmt%args))

def main():
    parser=argparse.ArgumentParser(description="HeatGuard AI server")
    parser.add_argument("--port",type=int,default=int(os.environ.get("PORT","8000")))
    parser.add_argument("--host",default=os.environ.get("HOST","0.0.0.0"))
    args=parser.parse_args()
    server=ThreadingHTTPServer((args.host,args.port),Handler)
    print(f"HeatGuard AI v{APP_VERSION} running on port {args.port}")
    try: server.serve_forever()
    except KeyboardInterrupt: print("\nStopped.")

if __name__=="__main__": main()
