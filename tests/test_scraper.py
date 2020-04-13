from polito_dl.scraper import get_videolesson_paths, get_course_name, get_professor_name

with open("tests/html/sviluppo_videolezioni_vis.html", "r") as fp:
    fake_course_page = fp.read()


def test_get_videolesson_paths():
    paths = get_videolesson_paths(fake_course_page)
    expected_paths = {
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21471",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22159",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21718",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21307",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22569",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22515",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21360",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21009",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21079",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21804",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21311",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22267",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22309",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22343",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22445",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21508",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22518",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22335",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22570",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21239",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21666",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21357",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22449",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21892",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21436",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22208",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21628",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22146",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21003",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21603",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21801",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=20957",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22028",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21156",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21149",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21733",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21512",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=19668",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21871",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21863",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21997",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=19638",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21604",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21100",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21749",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21665",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21232",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=20920",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22142",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22435",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=19726",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=19649",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21217",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21466",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22059",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22064",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22205",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=19818",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22271",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21478",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21099",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21935",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21430",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22524",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22437",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21927",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=20923",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=21994",
        "sviluppo.videolezioni.vis?cor=456&arg=Lezioni%20on-line&lez=22394",
    }
    assert set(paths) == expected_paths


def test_get_course_name():
    course_name = get_course_name(fake_course_page)
    assert course_name == "Algoritmi e programmazione"


def test_get_professor_name():
    professor_name = get_professor_name(fake_course_page)
    assert professor_name == "Paolo Enrico CAMURATI"
