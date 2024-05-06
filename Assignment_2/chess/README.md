# How to run

To play versus bot:

```
py chess.py play
```

To simulate a game between 2 bot with intelligence:

```
py chess.py sim <level:1-3>
```

To simulate a game between bot versus random moves:

```
py chess.py sim <level:1-3> white
```

```
py chess.py sim <level:1-3> black
```

# Game played

Level 2, White:

Moves: 1. Na3 e5 2. e3 Qh4 3. Nb5 b6 4. Nxc7+ Kd8 5. Nxa8 Nc6 6. Nxb6 axb6 7. Nf3 Qh6 8. Be2 Ke8 9. Rf1 Bd6 10. c3 Bc7 11. e4 Qf4 12. Nxe5 Qxe5 13. h3 d5 14. f4 Qxe4 15. d4 Nge7 16. Bd2 h5 17. Rc1 h4 18. a3 Qxg2 19. Bf3 Qg3+ 20. Ke2 Ba6+ 21. c4 Rh6 22. Bc3 Bxc4+ 23. Kd2 Bxf4+ 24. Kc2 Qg6+ 25. Be4 Qxe4+ 26. Qd3 Qxd3#

Review: 4 blunders !!!


# About (Vietnamese)

Với nhược điểm về độ phức tạp cao (n^d, trong đó n là số lượng nước đi hợp lệ, d là chiều sâu của thuật toán Minimax), thời gian để phân tích các nước đi với chiều sâu lớn trở nên rất lâu. Hiện tại, tác giả khuyến nghị độ sâu của giải thuật tối đa nên là 3 để đảm bảo thời gian tìm kiếm không quá lâu.

Về mặt không gian, vì sử dụng deep copy để tạo ra bản sao của bàn cờ mỗi khi cần phân tích một nước cờ mới nên độ phức tạp về mặt không gian cũng là n^d.
