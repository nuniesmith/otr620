# TomTom API & Pricing Reference

Source: [TomTom Pricing](https://docs.tomtom.com/pricing) (Retrieved September 2026)

## Overview
TomTom offers a generous free tier for developers with no credit card required upfront. Pricing is usage-based (pay-as-you-grow) with high monthly free request quotas per API.

---

## TomTom Maps vs. TomTom Orbis Maps

### TomTom Orbis Maps (Latest Generation)
* **Description:** TomTom's latest cloud-native map platform.
* **Features:** Richer map data, higher update frequency, and improved support for advanced use cases (EV routing, real-time traffic, precise geocoding).
* **Recommendation:** Use Orbis Maps for all new integrations to benefit from the latest features, performance improvements, and long-term support.

### TomTom Maps (Legacy Platform)
* **Description:** Previous-generation map platform.
* **Status:** Supported but being deprecated as equivalent or improved functionality is added to Orbis.

---

## Free Monthly Quotas by API

TomTom provides high-volume free monthly requests. Below is a breakdown of the free limits:

### 1. Map Display APIs
* **Map Display API Vector Tiles (Orbis):** **200,000 requests / month** free.
  * *Use case:* Serve and render vector tiles in your application.
* **Map Display API Raster Tiles (Orbis & Legacy):** **200,000 requests / month** free.
  * *Use case:* Serve and render raster tiles for map displays.
* **Map Display API Raster Non-Tile (Legacy):** **20,000 requests / month** free.

### 2. Navigation & Routing APIs
* **Routing API (Orbis & Legacy):** **20,000 requests / month** free.
  * *Use case:* Calculate optimal routes with traffic, vehicle settings (such as height/weight for large trucks), and waypoints.
* **Matrix Routing API (Legacy):** **2,500 requests / month** free.
  * *Use case:* Get travel times and distances for multiple origin-destination pairs.
* **Snap to Roads API (Legacy):** **2,500 requests / month** free.
  * *Use case:* Snap raw GPS traces to the road network and retrieve speed limits, lanes, etc.
* **Long Distance EV Routing API (Legacy):** **2,500 requests / month** free.
  * *Use case:* Plan EV trips with smart charging stops along the route.
* **Reachable Range API (Legacy):** **2,500 requests / month** free.
  * *Use case:* Calculate the reachable polygon from a given location.

### 3. Places & Search APIs
* **Places Search API Suggest (Orbis):** **10,000 requests / month** free.
  * *Use case:* Return place suggestions in real-time as users type.
* **Places Search API Details (Orbis):** **5,000 requests / month** free.
  * *Use case:* Retrieve detailed attributes for a single point of interest (POI).
* **Places Search API Discover (Orbis):** **5,000 requests / month** free.
  * *Use case:* Discover POIs and locations near a point.
* **Geocoding API (Orbis & Legacy):** **20,000 requests / month** free.
  * *Use case:* Convert textual addresses into geographic coordinates.
* **Reverse Geocoding API (Orbis & Legacy):** **20,000 requests / month** free.
  * *Use case:* Convert coordinates into human-readable addresses.

### 4. Traffic APIs
* **Traffic Incidents API Details (Orbis & Legacy):** **2,500 requests / month** free.
  * *Use case:* Retrieve real-time detailed incident data.
* **Traffic Flow & Incidents Vector/Raster Tiles (Orbis & Legacy):** **200,000 requests / month** free.
  * *Use case:* Render real-time traffic flows and incidents as tiles.
* **Traffic Flow API Segment Data (Legacy):** **20,000 requests / month** free.
  * *Use case:* Access speed and flow data at the individual road-segment level.

---

## Commercial & Automotive Only APIs
* **Fuel Prices API:** Contact Sales (Automotive only) - Get real-time fuel prices near any location.
* **Parking API:** Contact Sales (Automotive only) - Find parking availability, prices, and on-street spots.
* **Connected Services API, Traffic Stats, O/D Analysis, Junction Analytics, Area Analytics, Route Monitoring:** Contact Sales.
