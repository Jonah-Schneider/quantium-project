#Check that the visualisation is present.
from app import *
def graph_tester(dash_duo):
  #Start app running
  dash_duo.start_server(app)

  # wait for graph element
  graph = dash_duo.wait_for_element("#sales-graph")

  # confirm graph exists
  assert graph is not None

