
def pytest_addoption(parser):
    parser.addoption(
        "--provider", type=str, action="store",
        help="The provider name")
