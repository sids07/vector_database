def filter_search_results(results, thresh):
    final_results = []
    for i in results[0]:
        if i.distance >= thresh:
            final_results.append((i.entity.get('id'),i.entity.get('content_name'), i.distance))
    return final_results