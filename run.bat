pytest -s -v --capture=sys -m "sanity" --html=reports/reports.html testCases --browser_name chrome
REM pytest -s -v --capture=sys -m "sanity or regression" --html=reports/reports.html testCases --browser_name chrome
REM pytest -s -v --capture=sys -m "regression" --html=reports/reports.html testCases --browser_name chrome
REM pytest -s -v --capture=sys -m "sanity and regression" --html=reports/reports_chrome.html testCases --browser_name chrome

pytest -s -v --capture=sys -m "sanity" --html=reports/reports.html testCases --browser_name edge
REM pytest -s -v --capture=sys -m "sanity or regression" --html=reports/reports.html testCases --browser_name edge
REM pytest -s -v --capture=sys -m "regression" --html=reports/reports.html testCases --browser_name edge
REM pytest -s -v --capture=sys -m "sanity and regression" --html=reports/reports_edge.html testCases --browser_name edge