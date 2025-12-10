Feature: New example in examples_2

  Scenario: Cross-directory detection
    Given I have a feature in another directory
    When I run detection
    Then the detector should be able to find it


# in project root
python3 -m pip install --upgrade build wheel twine
rm -rf dist build *.egg-info
python3 -m build
# Test upload (recommended)
python3 -m twine upload --repository testpypi dist/*
# Production upload
python3 -m twine upload dist/*