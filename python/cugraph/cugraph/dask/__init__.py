# Copyright (c) 2020-2024, NVIDIA CORPORATION.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dask import config

from .link_analysis.pagerank import pagerank
from .link_analysis.hits import hits
from .traversal.bfs import bfs
from .traversal.sssp import sssp
from .common.read_utils import get_chunksize
from .common.read_utils import get_n_workers
from .community.louvain import louvain
from .community.triangle_count import triangle_count
from .community.egonet import ego_graph
from .community.induced_subgraph import induced_subgraph
from .centrality.katz_centrality import katz_centrality
from .components.connectivity import weakly_connected_components
from .sampling.uniform_neighbor_sample import uniform_neighbor_sample
from .sampling.random_walks import random_walks
from .centrality.eigenvector_centrality import eigenvector_centrality
from .cores.core_number import core_number
from .centrality.betweenness_centrality import betweenness_centrality
from .centrality.betweenness_centrality import edge_betweenness_centrality
from .cores.k_core import k_core
from .link_prediction.jaccard import jaccard
from .link_prediction.sorensen import sorensen
from .link_prediction.overlap import overlap
from .community.leiden import leiden

# Avoid "p2p" shuffling in dask for now
config.set({"dataframe.shuffle.method": "tasks"})
