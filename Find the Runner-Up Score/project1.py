"""
Given the participant's score sheet for your University Sports Day, you are

required to find the runner-up score. You have scores. Store them in a list and
find the score of the runner-up.

Sample input: [2, 3, 6, 6, 5]

Sample output: 5

Explanation: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second
maximum is 5. Hence, we print 5 as the runner-up score.
"""

scoresList = [2, 3, 6, 6, 5]

uniqueScores = list(set(scoresList))
uniqueScores.sort(reverse=True)

runnerUpScore = uniqueScores[1]
print(runnerUpScore)
