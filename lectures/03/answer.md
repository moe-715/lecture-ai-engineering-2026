# 第3回 解答

## 演習
- 第1回（素のLLM）とエージェントの回答の違い：data/glossary.jsonの中の内容を用いて回答している
- `--trace` で見えたツール呼び出し（ツール名と引数）：ツール名 search_glossary、引数 query
- 1つの質問での LLM 呼び出し回数（`requests`）：2回
- 追加したツールと、docstring に書いた説明：  
    - [search_glossary]
        講座の用語集から用語を検索し、定義と、どの回で扱うかを返す。
        AIエンジニアリングの用語や、この講座（AIE2026）に固有の言葉について
        答える前に使うこと。query には調べたい用語を1つだけ入れる（例: "LoRA"）。
        引数: {"query": {"type": "string"}}

    - [get_lecture_summary]
        指定した回（1始まりの整数）の講義の要点を返す。
        「第3回では何を学ぶ？」のように、回の内容や関係を聞かれたときに使う。
        引数: {"lecture": {"type": "integer"}}

    - [make_quiz]
        指定した回の用語から1つを選んで、確認問題と答えを返す。
        「第2回の確認問題を出して」のように、復習用の問題を求められたときに使う。
        まず lecture に一致する用語を絞り込み、そこから1つをランダムに選んで
        「用語の意味は？」という問題と、定義を返す。
        引数: {"lecture": {"type": "integer"}}

## 宿題
- 取り組んだレベル：基礎
- やったこと：
    - app/agent.py の"INSTRUCTIONS"と、app/tools.pyの"docstring"を1か所ずつ変更し、同じ質問(uv run python -m app.agent --trace "LoRAとQLoRAの違いは？")をして比較
    - 「必ず search_glossary で用語集を確認する」→「必要に応じて search_glossary で用語集を確認する」
    - 「query には調べたい用語を1つだけ入れる」→「query には調べたい用語をまとめて入れてもよいが、できるだけ1つの用語に絞る」
- 結果：
  - LoRAとQLoRA、search_glossaryが変わらず2回呼ばれてた
  - docstringにて、言い回しを変更したが、同じような回答となった
- 気づき：
  - 必要に応じて...できるだけ...のような言い回しはあまり効かない？言い回しよりも、具体的なツール使用方法みたいなところのが重要かと思われる
