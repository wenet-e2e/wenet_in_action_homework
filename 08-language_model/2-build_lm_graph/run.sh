#!/usr/bin/env bash
# Copyright 2022 Binbin Zhang(binbzha@qq.com)

[ ! -s tools] && ln -s WENET_DIR/tools
tools/fst/compile_lexicon_token_fst.sh dict tmp tmp2
tools/fst/make_tlg.sh lm tmp2 graph
rm -r tmp tmp2

# 生成 PDF
mkdir -p pdf
fstdraw --isymbols=graph/tokens.txt --osymbols=graph/tokens.txt graph/T.fst | dot -Tpdf -o pdf/T.pdf
fstdraw --isymbols=graph/tokens.txt --osymbols=graph/words.txt graph/L.fst | dot -Tpdf -o pdf/L.pdf
fstdraw --isymbols=graph/words.txt --osymbols=graph/words.txt graph/G.fst | dot -Tpdf -o pdf/G.pdf
fstdraw --isymbols=graph/tokens.txt --osymbols=graph/words.txt graph/LG.fst | dot -Tpdf -o pdf/LG.pdf
fstdraw --isymbols=graph/tokens.txt --osymbols=graph/words.txt graph/TLG.fst | dot -Tpdf -o pdf/TLG.pdf
