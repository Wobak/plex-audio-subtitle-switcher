import plex_set_tracks


def spoof_input(monkeypatch, inputList):
    """ Given a list of user input values, spoofs the input() function to to iterate over each item
        in the list with each successive call.

        Parameters:
            monkeypatch(MonkeyPatch): Monkeypatch from pytest.
            inputList(List<str>): List of input values to iterate over.
    """
    gen = (value for value in inputList)
    monkeypatch.setattr('builtins.input', lambda x: next(gen))


def test_get_num(monkeypatch):
    spoof_input(monkeypatch, ["7", "1024", "not_valid", "42"])
    assert int(plex_set_tracks.getNumFromUser("")) == 7
    assert int(plex_set_tracks.getNumFromUser("")) == 1024
    assert int(plex_set_tracks.getNumFromUser("")) == 42


def test_get_yes_or_no(monkeypatch):
    spoof_input(monkeypatch, ["y", "n", "not_valid", "y"])
    assert plex_set_tracks.getYesOrNoFromUser("") == "y"
    assert plex_set_tracks.getYesOrNoFromUser("") == "n"
    assert plex_set_tracks.getYesOrNoFromUser("") == "y"
