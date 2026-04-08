# Simple Shooting Game

Game giả lập bắn tank đơn giản cho dự án kiểm thử phần mềm.

## Chức năng hiện có

Di chuyển nhân vật, bắn đạn, kiểm tra và giải quyết va chạm.

## Chạy test

Cài đặt pytest: `pip install pytest pytest-cov`

Chạy:

Kiểm thử chức năng: `pytest blackbox_test.py`

Kiểm thử luồng điều khiển: `pytest cf_test.py --cov-report=html --cov-branch`  
Mở file `./htmlcov/function_index.html`, tìm hàm `Game.handle_collision` để xem chi tiết.

Kiểm thử luồng dữ liệu:
