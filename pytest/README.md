# Pytest Unit Testing
This folder contains unit tests written using the `pytest` framework. I am using these tests to validate the logic of Python functions (such as temperature conversion, physics calculations, and word scoring) that I built during my foundational exercises.
## QA-Driven Insights & Bug Fixes
Writing unit tests immediately surfaced behavior worth fixing:
*   **Case Sensitivity Bug:** Testing `score_word` initially revealed that lowercase words scored zero because the dictionary keys were uppercase. I caught this behavior through testing and fixed it by adding `.upper()` to handle input normalization.
*  **Scope of Testing & Negative Cases:** I initially left physically impossible inputs (such as negative mass) untested, since the functions had no validation. Revisiting this, I decided the calculation itself should reject invalid input, so I added a guard clause to get_force and covered it with pytest.raises.
*   **Data-Driven Tests:** Refactored repetitive tests into parametrized ones, keeping separate named tests where the name itself documented the case.
*   **Floating-Point Approximations:** Handled precision limits in temperature conversions using `pytest.approx()` to ensure reliable assertions.
## Contents
*   **`physics_class.py` & `test_physics_class.py`:** Validates mathematical functions for temperature, force, energy, and work calculations under various conditions (zero mass, negative acceleration, custom constants). 
*   **`scoring.py` & `test_scoring.py`:** Tests word score calculations, empty string edge cases, and lowercase input handling.
