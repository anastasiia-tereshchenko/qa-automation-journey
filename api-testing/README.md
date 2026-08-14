# API Testing Collection

## Collections

*   **objects-api-crud.json** — full CRUD lifecycle against restful-api.dev: create an object, retrieve it, replace it with PUT, update one field with PATCH, delete it, then confirm it's gone. Requests share state via a captured object ID.
*   **weather-api.json** — read-only tests against Open-Meteo: a valid forecast request, plus a negative case sending an out-of-range latitude and asserting the 400 response.

## QA-driven insights
*   **Type vs. Exact Assertions:** I learned that asserting exact values against live data (e.g., temperature) leads to flaky tests: an exact temperature assertion failed within ten minutes of being written. I switched to type assertions to ensure the API returns the expected data structure without failing due to dynamic content.
*   **PUT vs. PATCH:** I implemented paired assertions to distinguish between these methods.
    *  For PUT, I added a test to ensure the object is replaced (e.g., asserting that the old field data["CPU model"] does not exist).
    *  For PATCH, I added a test to ensure partial updates (e.g., pm.expect(jsonData.data).to.eql({ year: 2025, price: 1499.99 })), verifying that untouched fields remain present.
*   **Verification of DELETE:** I realised that receiving a 200 OK is not sufficient proof of deletion. I added a follow-up GET request; receiving a 404 Not Found is the true indicator that the resource has been successfully removed.
*   **Misleading status codes:** The objects API returns 405 Method Not Allowed when the daily rate limit is exceeded, rather than 429 Too Many Requests. The status code contradicts the error message, which would cause any automated check reading the status to misdiagnose the failure.

## How to run it
1. Download or clone the .json files.
2. Import the collections into Postman or your preferred API testing tool.
3. Configure your environment variables to supply your own API key (credentials are excluded from this repository for security purposes).
4. Run the collection in the specified order to ensure dependent requests are executed correctly.

## Note on ordering
The Objects Collection must be run top to bottom sequentially. Because these requests share state (the ID created in the first request is passed into subsequent PUT, PATCH, and DELETE requests), changing the order will cause tests to fail.
