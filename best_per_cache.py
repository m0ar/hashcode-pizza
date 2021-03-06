import tools
import sys
import parse

def solve_per_cache(max_cap, endpoints, S, req_dict):
    cache_eps = endpointsConnectedToCache(endpoints)
    all_solutions = {}
    for cache, eps in cache_eps.items():
        # brøds function for getting best videos for a cache
        pq = tools.top_videos_endpoints(eps, req_dict)
        idx = 0
        # As long as we can pick more, do so
        cap = max_cap
        while (idx < len(pq) and S[pq[idx][1]] <= cap):
            cap = cap - S[pq[idx][1]]
            idx = idx + 1
        solution = pq[:idx]
        req_dict = remove_vid_from_eps(solution, eps, req_dict)
        all_solutions[cache] = solution
    return all_solutions

def remove_vid_from_eps(vids, eps, req_dict):
    for (v, ep) in req_dict.items():
        if v in vids and ep in eps:
            del req_dict[(v,ep)]
    return req_dict

# Endpoints connected to cache
def endpointsConnectedToCache(endPoints):
  connectedCaches = {}
  for e in range(len(endPoints)):
    for cache, cache_lat in endPoints[e][1].items():
      if cache in connectedCaches:
        connectedCaches[cache].append(e)
      else:
        connectedCaches[cache] = [e]

  return connectedCaches

if __name__ == '__main__':
    filename = sys.argv[1]
    input = parse.parse(filename)
    endpoints = input[0]
    requests = input[1]
    params = input[2]

    solution = solve_per_cache(params['X'], endpoints, params['S'], requests)

    print(len(solution))
    for cache, vids in solution.items():
        string = " ".join(map(str, [vid[1] for vid in vids]))
        print(str(cache), string)
