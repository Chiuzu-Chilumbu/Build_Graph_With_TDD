from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GraphPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    VERTEX_INPUT = (By.ID, "vertex-input")
    EDGE_V1_INPUT = (By.ID, "vertex1")
    EDGE_V2_INPUT = (By.ID, "vertex2")
    ADD_EDGE_BUTTON = (By.XPATH, "//button[contains(text(), 'Add Edge')]") 
    ADD_VERTEX_BUTTON = (By.XPATH, "//button[contains(text(), 'Add Vertex')]") 
    BFS_BUTTON = (By.XPATH, "//button[contains(text(), 'BFS')]")
    DFS_BUTTON = (By.XPATH, "//button[contains(text(), 'DFS')]")
    STRUCTURE_CONTAINER = (By.ID, "structure-container")

    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        self.driver.find_element(*self.VERTEX_INPUT).send_keys(vertex)
        self.driver.find_element(*self.ADD_VERTEX_BUTTON).click()

    def add_edge(self, v1, v2):
        """Add an edge between two vertices"""
        self.driver.find_element(*self.EDGE_V1_INPUT).send_keys(v1)
        self.driver.find_element(*self.EDGE_V2_INPUT).send_keys(v2)
        self.driver.find_element(*self.ADD_EDGE_BUTTON).click()  

    def vertex_exists(self, vertex):
        """Check if a vertex exists"""
        return len(self.driver.find_elements(By.XPATH, f"//circle[@data-id='{vertex}']")) > 0

    def edge_exists(self, v1, v2):
        """Check if an edge exists"""
        return len(self.driver.find_elements(By.XPATH, f"//line[@data-edge='{v1}-{v2}']")) > 0 

