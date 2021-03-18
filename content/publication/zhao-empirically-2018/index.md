---
title: "Empirically Assessing Opportunities for Prefetching and Caching in Mobile Apps"
date: 2018-09-01
publishDate: 2019-09-22T22:47:42.155445Z
authors: ["Yixue Zhao", "Paul Wat", "Marcelo Schmitt Laser", "Nenad Medvidović"]
publication_types: ["1"]
abstract: "Network latency in mobile software has a large impact on user experience, with potentially severe economic consequences. Prefetching and caching have been shown effective in reducing the latencies in browser-based systems. However, those techniques cannot be directly applied to the emerging domain of mobile apps because of the differences in network interactions. Moreover, there is a lack of research on prefetching and caching techniques that may be suitable for the mobile app domain, and it is not clear whether such techniques can be effective or whether they are even feasible. This paper takes the first step toward answering these questions by conducting a comprehensive study to understand the characteristics of HTTP requests in over 1,000 popular Android apps. Our work focuses on the prefetchability of requests using static program analysis techniques and cacheability of resulting responses. We find that there is a substantial opportunity to leverage prefetching and caching in mobile apps, but that suitable techniques must take into account the nature of apps’ network interactions and idiosyncrasies such as untrustworthy HTTP header information. Our observations provide guidelines for developers to utilize prefetching and caching schemes in app development, and motivate future research in this area."
featured: false
publication: "*Proceedings of the 33rd ACM/IEEE International Conference on Automated Software Engineering* (**ASE**), acceptance rate: **19.9%** = 69/346"
tags: ["caching", "empirical study", "mobile apps", "network latency", "prefetching"]
url_pdf: "https://arxiv.org/abs/1810.08861"
doi: "10.1145/3238147.3238215"
url_code: "https://github.com/felicitia/PALOMA-Analysis/tree/empirical"
url_dataset:
url_poster:
url_project:
url_slides: "https://speakerdeck.com/yixue_zhao/empirically-assessing-opportunities-for-prefetching-and-caching-in-mobile-apps"
url_source:
url_video: "https://youtu.be/iT1pNy370ZM"
---

