from client import MctsGuidedChainOfThoughtReasoningTreeClient

def main():
    client = MctsGuidedChainOfThoughtReasoningTreeClient()
    res = client.explore_solution_tree('Optimize quantum circuit gate count for 64-qubit Shor algorithm modular exponentiation', 128)
    print('MCTS CoT Reasoning Tree: ' + res['reasoning_session_id'] + ' (Depth: ' + str(res['mcts_tree_depth_reached']) + ')')
    print('Branches Evaluated: ' + str(res['reasoning_branches_evaluated']) + ' | Pruned Paths: ' + str(res['backtracking_pruned_paths_count']))
    print('Confidence: ' + str(res['self_verification_confidence_pct']) + '%')
    print('Synthesis: ' + res['optimal_solution_synthesis'])
    print('Trace URL: ' + res['reasoning_graph_trace_url'])

if __name__ == '__main__':
    main()
