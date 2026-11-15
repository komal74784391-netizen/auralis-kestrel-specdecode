def schedule(draft_len, memory_budget):
    return min(draft_len, memory_budget // 16)
