# PRD: sgPostalCodes2017

## Overview
A Python script from 2017 that maps all Singapore postal codes to their geographic coordinates and addresses using the OneMap or Google Maps API. Stores results in `maps.txt` and/or output files. Educational data collection project demonstrating how to enumerate and geocode Singapore's postal code space.

## Goals
- Enumerate all valid Singapore postal codes (6-digit format)
- Geocode each postal code via mapping API (OneMap SG or Google Maps)
- Store results: postal code → coordinates (lat/lng) + address
- Output to text file(s) in `output/`

## Non-Goals
- Real-time postal code lookup service
- Web interface
- Address normalization or deduplication

## Tech Stack
- **Language**: Python 3.x (or Python 2.x — 2017)
- **Libraries**: `requests` (HTTP client for geocoding API)
- **APIs**: OneMap Singapore API or Google Maps Geocoding API

## Architecture
```
sgPostalCodes2017/
├── code/          # Geocoding scripts
├── output/        # Generated mapping files
├── maps.txt       # Sample or accumulated output
└── requirements.txt
```

## Deployment / Run
```bash
pip install -r requirements.txt
python code/<script>.py
```

## Constraints & Notes
- **2017 vintage**: API endpoints and authentication methods may have changed significantly
- **OneMap SG**: Singapore government's official geocoding service (preferred over Google Maps for SG postal codes)
- **Rate limiting**: Geocoding APIs have request limits; script likely needs sleep between calls
- **Coverage**: Singapore postal codes are 6 digits (000000-999999) but only a subset are valid; script may iterate all and filter by API response
