import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.acceptance_tests.pages.graph_page import GraphPage


pytestmark = pytest.mark.graph_acceptance_test


# TODO: Work on acceptance testing with SVG

# def test_add_vertex(driver, clear_graph, graph_page):
#     """Ensure graph starts fresh before adding a vertex."""
#     graph_page.add_vertex("B")

#     WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located(
#             (By.XPATH, "//*[local-name()='circle' and @data-id='A']")
#         )
#     )

#     assert graph_page.vertex_exists("B")


