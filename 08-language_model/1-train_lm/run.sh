#!/usr/bin/env bash
# Copyright 2022 Binbin Zhang(binbzha@qq.com)

ngram-count -order 2 -no-sos -no-eos -text train.txt -lm lm.arpa
cat lm.arpa
