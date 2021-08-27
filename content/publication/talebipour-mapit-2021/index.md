---
title: "UI Test Migration Across Mobile Platforms"
date: 2021-08-07
authors: ["Saghar Talebipour", 
"Yixue Zhao", "Luka Dojcilovic", "Chenggang Li",
"Nenad Medvidovic"]
# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]
abstract: "Writing UI tests manually requires significant effort. Several recent approaches have tried to address this problem in mobile apps: by exploiting the similarities of two different apps within the same domain (e.g., shopping apps) on a single platform (primarily Android), they have shown that it is possible to transfer tests that exercise similar functionality between the apps. An offshoot of this work has recently yielded a technique that transfers UI tests uni-directionally, from an open-source iOS app to the same app implemented for Android. This paper presents MAPIT, a technique that expands the existing body of work in three important ways: (1) MAPIT enables bi-directional UI test transfer between pairs of \"sibling\" Android and iOS apps; (2) MAPIT does not assume that the apps’ source code is available; (3) MAPIT is capable of transferring tests containing oracles in addition to UI events. MAPIT runs existing tests on a source app and builds an internal, partial model of the app corresponding to each test. The model comprises the user-visible features of the app (namely, screenshot bitmaps), the obtainable properties of each screenshot's constituent elements (e.g., widget IDs), and the labeled transitions between the screenshots. MAPIT uses this model to determine the corresponding information on the target app and generates an equivalent test, via a novel approach that leverages computer vision and natural language processing. Our evaluation on a diverse set of widely used, closed-source sibling Android and iOS apps shows that MAPIT is feasible, accurate, and useful in transferring UI tests across platforms."
featured: false
tags: ["mobile apps", "testing"]
publication: "*Proceedings of the 36th IEEE/ACM International Conference on Automated Software Engineering* (**ASE 2021**)"
#url_pdf: "https://arxiv.org/abs/2011.04654"
# doi: "10.1145/3368089.3409708"
#url_code: "https://github.com/felicitia/HiPHarness"
# url_dataset:
# url_poster: "files/PALOMA_Poster.pdf"
# url_project: "https://felicitia.github.io/PALOMA/"
#url_slides: "https://speakerdeck.com/yixue_zhao/assessing-the-feasibility-of-web-request-prediction-models-on-mobile-platforms"
# url_source:
#url_video: "https://youtu.be/91b3juLFbeU"
---

