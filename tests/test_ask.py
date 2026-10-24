from types import SimpleNamespace

from app import ask


def test_ask_prints_input_and_output_token_counts(monkeypatch, capsys):
    response = SimpleNamespace(
        usage_metadata=SimpleNamespace(prompt_token_count=12, candidates_token_count=7),
        text="回答",
    )

    class FakeModels:
        def generate_content(self, **kwargs):
            return response

    class FakeClient:
        models = FakeModels()

        def __init__(self, **kwargs):
            pass

    monkeypatch.setattr(ask.genai, "Client", FakeClient)
    monkeypatch.setattr(ask, "get_api_key", lambda: "test-key")

    assert ask.ask("質問") == "回答"
    assert "入力: 12, 出力: 7" in capsys.readouterr().out