# Feature file with description of queue operations

Feature: Created Queue class must be able to perform the basic operations

  Scenario: The queue class should be able to enqueue data onto the created deque
    Given a new created queue object
    When data is enqueued onto the queue
    Then the data should be added onto the queue

  Scenario: The queue class should be able to dequeue data from the created deque
    Given a queue with data in it
    When data is dequeued from the queue
    Then the data should be removed from the queue

  Scenario: The queue class should be able to check the size of the queue
    Given a queue containing data with a certain size
    When the size of the queue is checked
    Then the queue should return the size of the queue which is equivalent to the number of data in the queue

  Scenario: The queue class should be able to check if the queue is empty
    Given a queue object contains no data
    When the queue is checked if it is empty
    Then the queue should return True when empty

  Scenario: The queue class should be able to check if the queue is full
    Given a queue where the size is equal to the given capacity
    When the queue is checked if it is full
    Then the queue should return True when full
