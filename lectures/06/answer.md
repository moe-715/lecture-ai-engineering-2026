# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：glossary_search_glossary
- STEP 2 の [tool call]：glossary_search_glossary({'query': '3レベル'})
- STEP 3 の [tool call]：fetch_fetch({'url': 'https://modelcontextprotocol.io/'})
- STEP 4 の [tool call]：aws_aws___search_documentation({'topics': ['general'], 'search_phrase': 'Amazon S3 バージョニング 概要'})、aws_aws___search_documentation({'topics': ['general'], 'search_phrase': 'Using versioning in S3 buckets'})
- 気づき・疑問：MCP、設定ファイルを変更するだけでエージェント利用できるので、複数使用していても一箇所変更するだけで良いというのは修正の手間が省けていい

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：基礎
- やったこと：app/mcp_server.pyにてserver.tool()(tools.get_lecture_summary)を追記して、この関数を新たなMCPのツールとして公開することができるか確認する
- 結果：返答として、追加前は[glossary_search_glossary]だけだったが、追加後[glossary_get_lecture_summary]が増えていることを確認！ [tool call]   glossary_get_lecture_summary({'lecture': 2})
- 気づき・疑問：自分の管理下のMCPサーバーであれば、サーバー側のどのツールを公開するかを設定できる
