---
title: "Assessing the Feasibility of Web-Request Prediction Models on Mobile Platforms"
date: 2021-03-31
authors: ["Yixue Zhao", 
"Siwei Yin", 
"Adriana Sejfia", 
"Marcelo Schmitt Laser", 
"Haoyu Wang", 
"Nenad Medvidovic"]
# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]
abstract: "Prefetching web pages is a well-studied solution to reduce network latency by predicting users' future actions based on their past behaviors. However, such techniques are largely unexplored on mobile platforms. Today's privacy regulations make it infeasible to explore prefetching with the usual strategy of amassing large amounts of data over long periods and constructing conventional, \"large\" prediction models. Our work is based on the observation that this may not be necessary: Given previously reported mobile-device usage trends (e.g., repetitive behaviors in brief bursts), we hypothesized that prefetching should work effectively with \"small\" models trained on mobile-user requests collected during much shorter time periods. To test this hypothesis, we constructed a framework for automatically assessing prediction models, and used it to conduct an extensive empirical study based on over 15 million HTTP requests collected from nearly 11,500 mobile users during a 24-hour period, resulting in over 7 million models. Our results demonstrate the feasibility of prefetching with small models on mobile platforms, directly motivating future work in this area. We further introduce several strategies for improving prediction models while reducing the model size. Finally, our framework provides the foundation for future explorations of effective prediction models across a range of usage scenarios."
featured: true
tags: ["mobile platforms", "prediction", "network latency"]
publication: "*Proceedings of the 8th IEEE/ACM International Conference on Mobile Software Engineering and Systems 2021* (**MOBILESoft**)"
url_pdf: "https://arxiv.org/abs/2011.04654"
# doi: "10.1145/3368089.3409708"
url_code: "https://github.com/felicitia/HiPHarness"
# url_dataset:
# url_poster: "files/PALOMA_Poster.pdf"
# url_project: "https://felicitia.github.io/PALOMA/"
# url_slides: "https://speakerdeck.com/yixue_zhao/fruiter-a-framework-for-evaluating-ui-test-reuse"
# url_source:
# url_video: "https://youtu.be/zVWpT5aLyQo"
---

