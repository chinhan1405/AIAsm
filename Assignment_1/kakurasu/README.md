# How to run

You can run the Kakurasu solver by running kakurasu_dfs.py for DFS solution or kakurasu_mrv.py for MRV solution.

To solve a new Kakurasu problems, please define it in a new input.txt file and put it into 'kakurasu/testcase/' folder, and then adjust the INPUT_FILE constant in kakurasu_dfs.py or kakurasu_mrv.py to the path to your new Sudoku problems.

DFS version:
```
    py kakurasu_dfs.py
    py kakurasu_dfs2.py
```

MRV version:
```
    py kakurasu_mrv.py
```


# About (Vietnamese)

## Về thời gian

Lý giải về cách tiếp cận bài toán đầu tiên, mỗi trạng thái sẽ được sinh ra từ trạng thái trước bằng cách tô đen 1 ô. Khi áp dụng giải thuật Depth First Search với cách tiếp cận này, ta thấy được độ phức tạp của giải thuật sẽ là O(2^(n^2)) với n là cạnh của bảng Kakurasu nxn. Khi n lên tới 5, số bước giải trong trường hợp tệ nhất có thể lên tới 33554432 bước! Nếu kết hợp với kĩ thuật Pruning để cắt bỏ ngay tại những trạng thái có tổng của hàng hoặc cột đã vượt quá giá trị mục tiêu, thời gian thực thi sẽ giảm đi đáng kể. Nhờ vào kĩ thuật Pruning, giải thuật Depth First Search có thể giải tới bài toán Kakurasu 6x6 trong thời gian thực tế. 

Ở cách tiếp cận thứ 2, ta sẽ chia giải thuật làm 2 bước:
    Bước 1: Tìm các tổ hợp có thể xảy ra trong từng hàng của bảng Kakurasu.
    Bước 2: Từ bảng tổng hợp từ bước 1, ta thay từng tổ hợp của các tổ hợp này vào bảng Kakurasu và kiểm tra xem các có thỏa mãn giá trị mục tiêu hay không.

Việc tìm các tổ hợp của từng hàng trong bảng Kakurasu sử dụng phương pháp Backtracking là không quá phức tạp và không tốn nhiều thời gian. Mỗi hàng thường không có quá nhiều tổ hợp nên độ phức tạp sẽ thấp hơn cách tiếp cận đầu tiên. Cách tiếp cận mới đã giảm mạnh thời gian thực thi và có thể giải tới bài toán Kakurasu 7x7 trong thời gian thực tế.

Bằng kĩ thuật heuristic Minimum Remaining Values, ta sẽ ưu tiên xét các hàng có số lượng tổ hợp thấp nhất. Kết hợp với kĩ thuật Backtracking và Pruning ta sẽ giải được bài toán Kakurasu 9x9 với thời gian thực thi chấp nhận được và khá ổn định.

## Về không gian

Giải thuật Depth First Search cần lưu trữ các trạng thái đã gặp vào danh sách visited và stack, do đó có độ phức tạp về không gian sẽ gần như độ phức tạp về thời gian. Từ đây ta có thể thấy Depth First Search không phù hợp để giải bài toán Kakurasu.

Với giải thuật áp dụng Heuristic, ta có thể cải tiến khi sử dụng Backtracking, tức là ta sẽ chỉ thao tác trên duy nhất một bảng dữ liệu Kakurasu.

