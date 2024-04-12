# How to run

You can run the Sudoku solver by running sudoku_dfs.py for DFS solution or sudoku_mrv.py for MRV solution.

To solve a new Sudoku problems, please define it in a new input.txt file and put it into 'sudoku/testcase/' folder, and then adjust the INPUT_FILE constant in sudoku_dfs.py or sudoku_mrv.py to the path to your new Sudoku problems.


## About (Vietnamese)

# Về thời gian

Giải thuật Depth First Search cho bài toán Sudoku có độ phức tạp là O(n^(m^2)) với n là chiều rộng của bảng Sudoku và m là số ô trống cần điền trên bảng. Giải thuật phải xét n giá trị khác nhau vào n^2 ô và kiểm tra tính hợp lệ của từng trường hợp. Với cách giải này, ngay cả trường hợp Sudoku 4x4 có 8 ô trống như testcase đầu tiên cũng cần tới 65536 bước để giải bài toán trong trường hợp tệ nhất, và con số này lên tới 9^49 trong bài toán Sudoku 9x9 có 49 ô trống!
Để giảm bớt số bước trên và giảm thời gian thực thi, ta có thể kết hợp kĩ thuật Pruning. Bằng việc áp dụng Pruning vào giải thuật, ta sẽ chỉ sinh ra các trạng thái mới từ các trạng thái hợp lệ (tức là chưa có hàng, cột hay khu vực nào có 2 ô trùng giá trị). Kĩ thuật này đã cải thiện đáng kể thời gian thực thi, giúp cho giải thuật có thể giải được một bài toán Sudoku 4x4 trong thời gian chấp nhận được.
Tuy nhiên thời gian thực thi cho trường hợp Sudoku 9x9 vẫn còn quá lớn, ta không thể tiếp tục với cách tiếp cận bằng Depth First Search đơn thuần được nữa mà phải kết hợp với Heuristic.
Bằng kĩ thuật heuristic Minimum Remaining Values, ta sẽ ưu tiên thử cho các ô có ít giá trị hợp lệ nhất. Kết hợp với Backtracking và Pruning, ta sẽ có thể giải được bài toán Sudoku 9x9 trong thời gian chấp nhận được. Tuy nhiên thời gian thực thi của giải thuật này sẽ không ổn định do vẫn giữ tính chất của quay lui nhưng vẫn sẽ nằm trong khoảng chấp nhận được.

# Về không gian

Giải thuật Depth First Search cần lưu trữ các trạng thái đã gặp vào danh sách visited và stack, do đó có độ phức tạp về không gian sẽ gần như độ phức tạp về thời gian. Từ đây ta có thể thấy Depth First Search không phù hợp để giải bài toán Sudoku.
Với giải thuật áp dụng Heuristic, ta có thể cải tiến khi sử dụng Backtracking, tức là ta sẽ chỉ thao tác trên duy nhất một bảng dữ liệu Sudoku.

