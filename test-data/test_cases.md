# HeatGuard AI – Synthetic Test Dataset

All cases below are synthetic and are not live forecasts or official warnings. TC-01 to TC-10 are the proposed Milestone 2 test set. Only tests actually executed in Google AI Studio should be marked with actual outputs and Pass/Fail.

## TC-01 – Normal / Advisory Generation
- Input: Hot and dry conditions are expected during the afternoon.
- Location: Not provided
- Date/period: Not provided
- Temperature/warning: Not provided
- Audience: General public
- Expected: Generate a short advisory, include general precautions, and state missing temperature/date/location/warning level.

## TC-02 – Normal / Advisory Generation
- Input: Temperature is expected to reach 42°C during the afternoon.
- Location: Not provided
- Date/period: Not provided
- Temperature/warning: 42°C
- Audience: General public
- Expected: Preserve 42°C; do not invent date/location/warning level; state missing fields.

## TC-03 – Normal / Advisory Generation
- Input: Hot and dry conditions are expected on 25 November 2026 in Hyderabad.
- Location: Hyderabad
- Date/period: 25 November 2026
- Temperature/warning: Not provided
- Audience: General public
- Expected: Preserve supplied date/location; do not invent temperature/warning level.

## TC-04 – Normal / Audience Adaptation
- Input: Hot and dry conditions are expected during the afternoon.
- Location: Not provided
- Date/period: Not provided
- Temperature/warning: Not provided
- Audience: College students
- Expected: Adapt for classes, campus walking and sports without changing forecast facts.

## TC-05 – Normal / Audience Adaptation
- Input: Hot conditions are expected during the afternoon; maximum temperature is 41°C on 26 November 2026.
- Location: Hyderabad
- Date/period: 26 November 2026
- Temperature/warning: 41°C
- Audience: Campus administrators
- Expected: Adapt for campus planning; do not invent official warning level.

## TC-06 – Normal / Advisory Generation
- Input: Hot and dry conditions are expected during the afternoon.
- Location: Hyderabad
- Date/period: 27 November 2026
- Temperature/warning: 43°C; Yellow alert supplied
- Audience: General public
- Expected: Preserve supplied temperature/date/location/Yellow alert exactly; no invented details.

## TC-07 – Edge / Advisory Generation
- Input: [EMPTY FORECAST TEXT]
- Location: Not provided
- Date/period: Not provided
- Temperature/warning: Not provided
- Audience: General public
- Expected: Ask for forecast information or state that no advisory can be grounded; do not invent weather facts.

## TC-08 – Edge / Advisory Generation
- Input: Hot conditions are expected.
- Location: Not provided
- Date/period: Not provided
- Temperature/warning: Not provided
- Audience: General public
- Expected: Explicitly state that date, location, temperature and warning level are absent; no assumptions.

## TC-09 – Edge / Output Review
- Input: Original forecast A: Hot and dry afternoon expected. Original forecast B: Cool and rainy afternoon expected.
- Location: Not provided
- Date/period: Not provided
- Temperature/warning: Conflicting source statements
- Audience: General public
- Expected: Flag contradictory source information and request clarification; do not choose one as fact.

## TC-10 – Invalid / Output Review
- Input: Original forecast: Hot and dry conditions are expected during the afternoon. Generated advisory: 45°C tomorrow in Hyderabad; official red alert issued.
- Location: Not provided
- Date/period: Not provided
- Temperature/warning: Not provided
- Audience: Not specified
- Expected: Flag invented 45°C, date, location and official alert; identify omitted dry conditions and reject.
