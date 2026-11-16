# Quy ước viết commit (Conventional Commits)

## 1. Format

```
<type>(<scope>): <mô tả ngắn>

[body - không bắt buộc]

[footer - không bắt buộc]
```

| Phần | Bắt buộc | Ý nghĩa |
|------|----------|---------|
| `type` | Có | Loại thay đổi (xem bảng mục 2) |
| `scope` | Không | Phần bị ảnh hưởng: `auth`, `api`, `ui`, `db`... |
| `mô tả ngắn` | Có | Tóm tắt thay đổi, dưới 72 ký tự |
| `body` | Không | Giải thích **vì sao** và **thay đổi gì**, cách tiêu đề 1 dòng trống |
| `footer` | Không | Liên kết issue (`Closes #12`) hoặc `BREAKING CHANGE: ...` |

## 2. Các type hay dùng

| Type | Dùng khi | Ví dụ |
|------|----------|-------|
| `feat` | Thêm tính năng mới | `feat(auth): add login with Google` |
| `fix` | Sửa bug | `fix(cart): correct total price calculation` |
| `docs` | Chỉ sửa tài liệu (README, comment, wiki) | `docs: update installation guide` |
| `style` | Format code, không đổi logic (dấu cách, chấm phẩy, prettier) | `style: format code with prettier` |
| `refactor` | Viết lại code, không thêm tính năng, không sửa bug | `refactor(user): extract validation to helper` |
| `perf` | Cải thiện hiệu năng | `perf(api): cache product list query` |
| `test` | Thêm hoặc sửa test | `test(auth): add unit tests for login service` |
| `build` | Thay đổi build tool, dependency (npm, maven, webpack) | `build: upgrade react to v19` |
| `ci` | Thay đổi cấu hình CI/CD (GitHub Actions, Jenkins) | `ci: add deploy workflow` |
| `chore` | Việc lặt vặt không đụng tới code chạy hay test (.gitignore, config) | `chore: update .gitignore` |
| `revert` | Hoàn tác một commit trước đó | `revert: feat(auth): add login with Google` |

## 3. Quy tắc viết mô tả

- Dùng động từ nguyên mẫu ở đầu: `add`, `fix`, `update`, `remove` (không dùng `added`, `fixes`).
- Không viết hoa chữ cái đầu, không có dấu chấm ở cuối.
- Mỗi commit chỉ làm **một việc**. Vừa sửa bug vừa thêm tính năng thì tách thành 2 commit.
- Viết thống nhất một ngôn ngữ trong cả repo (thường là tiếng Anh).

## 4. Breaking change

Thay đổi làm hỏng code cũ (đổi API, xóa hàm, đổi cấu trúc DB) thì thêm `!` sau type hoặc ghi ở footer:

```
feat(api)!: change response format of /users

BREAKING CHANGE: field `name` is split into `firstName` and `lastName`
```

## 5. Ví dụ đầy đủ

Commit một dòng:

```bash
git commit -m "feat(student): add search by name"
```

Commit có body và footer:

```bash
git commit -m "fix(route): prevent duplicate bus assignment" -m "A bus could be assigned to two routes at the same time because the check only compared route id." -m "Closes #24"
```

Kết quả:

```
fix(route): prevent duplicate bus assignment

A bus could be assigned to two routes at the same time because
the check only compared route id.

Closes #24
```

## 6. Đặt tên branch (đi kèm)

```
<type>/<mô-tả-ngắn>
```

| Branch | Dùng cho |
|--------|----------|
| `feat/login-google` | Tính năng mới |
| `fix/cart-total` | Sửa bug |
| `docs/readme` | Tài liệu |
| `refactor/user-service` | Refactor |
| `hotfix/payment-crash` | Sửa gấp trên production |

## 7. Bảng tra nhanh

```
feat:     tính năng mới
fix:      sửa bug
docs:     tài liệu
style:    format, không đổi logic
refactor: viết lại code
perf:     tối ưu hiệu năng
test:     test
build:    build tool, dependency
ci:       CI/CD
chore:    việc lặt vặt
revert:   hoàn tác commit
```
