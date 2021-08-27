---
title: "Identifying Casualty Changes in Software Patches"
date: 2021-06-07
authors: [ "Adriana Sejfia", 
"Yixue Zhao",  
"Nenad Medvidovic"]
# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]
abstract: "Noise in software patches impacts their understanding, automated analysis, and use for tasks such as change prediction. Although several approaches have been developed to identify noise in patches, this issue has persisted. An analysis of a recently published dataset of security patches for the Tomcat web server, which we further expanded with security patches from five additional systems, uncovered several kinds of previously unreported noise which we call casualty changes. These are changes that themselves do not alter the logic of the program but are necessitated by other changes made in the patch. In this paper, we provide a comprehensive taxonomy of casualty changes. We then develop CasCADe, an automated technique for automatically identifying casualty changes. We evaluate CasCADe with several publicly available datasets of patches and tools that focus on them. Our results show that CasCADe is highly accurate, that the kinds of noise it identifies occur relatively commonly in patches, and that removing this noise improves upon the evaluation results of previously published approaches."
featured: false
tags: ["security", "software patches", "program analysis"]
publication: "*Proceedings of the 29th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering* (**ESEC/FSE 2021**)"
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

