---
title: "Avgust: Automating Usage-Based Test Generation from Videos of App Executions"
date: 2022-06-12
authors: ["Yixue Zhao", "Saghar Talebipour", "Kesina Baral", "Hyojae Park", "Leon Yee", "Safwat Ali Khan", "Yuriy Brun",
"Nenad Medvidovic", "Kevin Moran"]
# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]
abstract: "Writing and maintaining UI tests for mobile apps is a time-consuming and tedious task. While decades of research have produced automated approaches for UI test generation, these approaches typically focus on testing for crashes or maximizing code coverage. By contrast, recent research has shown that developers prefer usage-based tests, which center around specific uses of app features, to help support activities such as regression testing. Very few existing techniques support the generation of such tests, as doing so requires automating the difficult task of understanding the semantics of UI screens and user inputs. In this paper, we introduce Avgust, which automates key steps of generating usage-based tests. Avgust uses neural models for image understanding to process video recordings of app uses to synthesize an app-agnostic state-machine encoding of those uses. Then, Avgust uses this encoding to synthesize test cases for a new target app. We evaluate Avgust on 374 videos of common uses of 18 popular apps and show that 69% of the tests Avgust generates successfully execute the desired usage, and that Avgust's classifiers outperform the state of the art."
featured: true
tags: ["software testing", "AI/ML", "UI understanding"]
publication: "*Proceedings of the 30th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering* (**ESEC/FSE 2022**)"
url_pdf: "https://arxiv.org/abs/2209.02577"
doi: "10.1145/3540250.3549134"
url_code: "https://doi.org/10.5281/zenodo.7036218"
# url_dataset:
# url_poster: "files/PALOMA_Poster.pdf"
# url_project: "https://felicitia.github.io/PALOMA/"
url_slides: "https://speakerdeck.com/yixue_zhao/avgust-automating-usage-based-test-generation-from-videos-of-app-executions"
# url_source:
url_video: "https://youtu.be/LB-TrLhQcvI"
---

