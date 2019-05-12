"""
자료 구조 (data structure)는 메모리의 자료를 저장할 수 있는 여러가지 방법을 말한다. 각각의 자료 구조마다 가지고 있는
장점과 단점이 다르기 때문에, 문제 해결을 위해 적절한 자료 구조를 사용하는 것은 매우 중요하다. 자료 구조를 직접 구현하는
대신 표준 라이브러리를 사용하면 많은 시간을 절약할 수 있다.

1. 동적 배열 (dynamic array)
- 프로그램 실행 중에 크기를 변경할 수 있는 배열을 동적 배열이라고 한다. Rust의 대표적인 동적 배열 자료 구조로는
`std::vec::Vec`이 있다. ("A contiguous growable array type, written `Vec<T>` but pronounced 'vector'.")
- 동적 배열의 내부에는 배열이 들어있으며 필요할 때마다 이 배열의 크기를 늘려서 사용한다.
- Rust의 `std::string::String`도 동적 배열의 한 종류라고 할 수 있다.

2. 집합 (set)
- 집합은 여러 개의 원소를 가지고 있는 자료 구조로, 집합의 대표적인 기능으로는 원소 삽입과 검색, 삭제 등이 있다.
- 집합의 가장 중요한 특징은 집합의 모든 원소는 서로 다른 값을 가지고 있다는 것이다.

3. 맵 (map)
- 맵은 키와 값의 순서쌍으로 이루어진 일반화된 배열이다.

4. 반복자 (iterator)
- 반복자는 어떤 자료 구조의 원소를 가리키는 변수를 말한다.

5. 덱 (deque)
- 덱은 동적 배열과 비슷하지만, 배열의 앞과 뒤 모두에 원소를 삽입하는 것이 가능하다. 덱은 동적 배열보다 더 복잡하게 구현
이 되어 있기 때문에, 덱은 벡터보다 처리 속도가 대체로 느린 것이 알려져 있다. 원소를 삽입하거나 삭제할 때의 시간 복잡도는
대체로 `O(1)`로 동적 배열과 같다.

6. 스택 (stack)
- 스택은 시간 복잡도가 `O(1)`인 두 개의 기능, 맨 위에 원소 삽입하기와 맨 위로부터 원소 삭제하기를 제공하는 자료 구조로,
항상 맨 위에 있는 원소만 접근할 수 있다.

7. 큐 (queue)
- 큐 또한 시간 복잡도가 `O(1)`인 두 개의 기능, 큐의 맨 뒤에 원소 삽입하기와 큐의 맨 앞에 있는 원소 삭제하기를 
제공하는 자료 구조이다. 큐에서는 항상 첫 번째 원소와 맨 마지막 원소에만 접근할 수 있다.

8. 연결 리스트 (linked list)
- 연결 리스트는 구조체가 사슬처럼 연결되어 있는 구조를 가지는데, 연결 리스트의 각 구조체를 노드 (node)라고 한다. 하나의
노드는 그 다음 노드의 포인터를 가지고 있으며, 마지막 노드는 아무것도 가리키지 않는 널 포인터로 되어 있다. 연결 리스트는
배열보다 크기를 늘리거나 줄이는 것이 더 쉽다는 장점이 있지만, 연결 리스트의 원소에 접근할 때 노드가 맨 마지막 노드와
가까울수록 접근 속도가 느려진다는 단점이 있다.

* https://docs.python.org/3/tutorial/datastructures.html
* https://stackoverflow.com/questions/10974922/what-is-the-basic-difference-between-stack-and-queue
"""

from collections import deque

if __name__ == '__main__':
    dyn_arr = [1, 2, 3, 4, 5]

    # To create an empty set, you have to use `set()`, not `{}`; the latter creates an empty dictionary, a data structure.
    set = {'apple', 'banana', 'lemon', 'kiwi', 'pineapple'}

    map = {
        'apple': 1000,
        'banana': 1200,
        'lemon': 1400,
        'kiwi': 1600,
        'pineapple': 1700
    }

    deq = deque([2, 3, 4])

    dyn_arr.append(6)
    dyn_arr.reverse()
    dyn_arr.pop()

    del map['pineapple']

    for x, y in zip([1, 2, 3], [4, 5, 6]):
        print(f"x: {x}, y: {y}")

    deq.appendleft(1)
    deq.append(5)
