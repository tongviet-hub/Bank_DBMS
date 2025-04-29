# CSDL-Bank
# GIỚI THIỆU
Ngày nay, việc giao dịch tiền tệ với Ngân hàng đã trở nên phổ biến đối với mọi 
người, nhất là ở những khu vực có kinh tế năng động và phát triển nhanh.
Ngân hàng và những chi nhánh mọc lên ở nhiều nơi và thúc đẩy sự đi lên của nền 
kinh tế. Chúng ta có thể thấy hàng loạt các Ngân hàng lớn nhỏ như: Agribank, 
Vietcombank, VietinBank, SacomBank, DongABank, SeaBank, TechcomBank, 
IndoVinaBank, MilitaryBank, EximBank, SaigonCommercialBank, …Vì thế, hơn 
bất cứ lĩnh vực nào, hoạt động của Ngân hàng luôn phải đặt trong một môi trường 
cạnh tranh. Để tồn tại và đi lên trong môi trường đó, bắt buộc mọi Ngân hàng cần 
phải luôn phát triển đạt đến mục tiêu tạo vốn cho xã hội và làm giàu cho chính 
mình. Do vậy mỗi Ngân hàng luôn thay đổi chính sách và cơ chế hoạt động sao 
cho chặt chẽ, tiết kiệm và đơn giản nhất. Một trong những thay đổi thiết thực và 
cấp bách là việc tối ưu hóa nghiệp vụ tiền gửi thông qua các công cụ mạnh mẽ của 
Công nghệ Thông tin.
Bên cạnh đó, cùng với tốc độ phát triển chóng mặt của công nghệ, tội phạm mạng 
cũng ngày càng gia tăng về số lượng cũng như hình thức ngày càng tinh vi hơn. 
Điều này đặt ra một thách thức lớn cho các Ngân hàng trong việc bảo vệ cơ sở dữ
liệu của mình trước những nguy cơ rất lớn về đánh cắp thông tin và tấn công máy 
chủ. Đảm bảo uy tín, lợi nhuận và tính liên tục trong kinh doanh của Ngân hàng 
mình.
Do đó nhóm chọn đề tài này để bên cạnh việc học hỏi thêm kinh nghiệm, bổ sung 
kiến thức cần thiết cho chính mình, nhóm còn muốn tìm hiểu việc tạo ra một hệ
thống tối ưu về dữ liệu, đơn giản trong thao tác, bảo mật an toàn trước những mối 
nguy hiểm của tin tặc,… với tiêu chí hàng đầu là “Keep it simple, stupid!”. Hy 
vọng là những gì nhóm làm được sẽ giúp ích một phần nhỏ nào đó trong việc hoàn 
thiện hệ thống tin học trong Ngân hàng.
# MÔ TẢ ĐỀ TÀI
### I. Đặt vấn đề
Một Ngân hàng cần xây dựng hệ thống quản lý tiền gửi cho Ngân hàng mình 
như sau:
Trong Ngân hàng có nhiều cấp bậc chức vụ nhưng chủ yếu ở đây là: quản lý, 
nhân viên tín dụng và người quản trị tương ứng với ba loại phân quyền trong hệ
thống.
Hệ thống sẽ quản lý các thông tin cơ bản của nhân viên và quyền hạn khi sử
dụng phần mềm.
Khi khách hàng đến Ngân hàng để gửi tiền lần đầu tiên, người gửi được lập một 
tài khoản. Mỗi Tải khoản có một mã số gọi là số tài khoản và mỗi ngưởi tại một 
thời điểm chỉ có duy nhất một tài khoản trong Ngân hàng. Một Tài khoản có 
thể có một hay nhiều Sổ tiết kiệm với các loại tiết kiệm và loại tiền gửi khác 
nhau. 
Khách hàng có thể tiền gửi bằng tiền Đôla (USD) hoặc bằng tiền Việt Nam 
(VND). Khi có nhu cầu gửi tiền, người gửi phải viết một giấy gửi tiền rồi đưa 
cho nhân viên tín dụng cùng số tiền định gửi, trong giấy gửi tiền có những 
thông tin sau : họ tên người gửi, địa chỉ, số CMND, số tiền (bằng số & bằng 
chữ), loại tiền, ngày gửi, loại tiết kiệm, …
Nhân viên tín dụng căn cứ vào giấy gửi tiền và số tiền lập một Sổ tiết kiệm, liên 
kết nó với Tài khoản của khách hàng và viết cho người gửi một giấy biên nhận, 
số phiếu của giấy biên nhận sẽ phải giống số phiếu của giấy gửi tiền. 
Nếu khách hàng muốn gửi thêm tiền vào Sổ tiết kiệm không kỳ hạn (tiền phải 
cùng loại với tiền trong Sổ tiết kiệm đó), người gửi phải viết một giấy gửi tiền 
rồi đưa cho nhân viên tín dụng cùng số tiền định gửi, trong giấy gửi tiền có 
những thông tin sau : họ tên người gửi, địa chỉ, số CMND, số tiền (bằng số & 
bằng chữ), số Sổ tiết kiệm, … Nhân viên tín dụng căn cứ vào giấy gửi tiền và 
số tiền cập nhật lại Sổ tiết kiệm và viết cho người gửi một giấy biên nhận, số
phiếu của giấy biên nhận sẽ phải giống số phiếu của giấy gửi tiền.
Khi hết thời hạn gửi tiền, nếu người gửi đến thanh toán thì toàn bộ số tiền cả
gốc và lãi của họ sẽ được trả lại họ kèm theo một giấy thanh toán, trường hợp 
khách hàng bị mất Sổ tiết kiệm thì họ có thể dùng CMND để tra cứu vào Tài 
khoản và rút tiền trong Sổ tiết kiệm mình mong muốn. Sau đó nếu người gửi 
muốn gửi tiếp họ sẽ được lập Sổ mới. Nếu hết kỳ hạn mà người gửi không đến 
thanh toán thì số tiền lãi của họ sẽ được cộng vào số tiền gốc và coi như họ tiếp 
tục gửi tiền với số tiền gốc mới và kì hạn là như cũ với Sổ tiết kiệm cũ. Nếu 
chưa đến kì hạn rút tiền mà người gửi muốn rút tiền đã gửi về thì tuỳ theo 
khoảng thời gian đã gửi ở mức nào mà khách hàng được tính lãi theo tỷ lệ ở
mức đó.
Tùy từng thời điểm, căn cứ vào tình hình thực tế của Ngân Hàng sẽ có thay đổi 
tỷ lệ lãi suất tín dụng. Có một số mức gửi như sau: không kì hạn, 1 tháng, 3 
tháng, 6 tháng, 9 tháng, 18 tháng, 24 tháng, 36 tháng. Tuỳ theo mức gửi sẽ có tỉ
lệ lãi suất tương ứng.
Hệ thống sẽ ghi nhận tất cả các thao tác của người dùng đối với Tài khoản và 
Sổ tiết kiệm, hỗ trợ tra cứu, thống kê, theo dõi tình trạng tiển gửi, bảo mật và 
phục hồi dữ liệu khi có sự cố.
### II. Yêu cầu chức năng
1.2.1. Yêu cầu lưu trữ:
 Hệ thống cần lưu trữ các thông tin liên quan đến nhân viên, tài 
khoản, sổ tiết kiệm, quy định, thông tin đăng nhập, phân quyền 
người dùng, nhật ký thao tác tài khoản, nhật ký thao tác sổ tiết kiệm.
1.2.2. Yêu cầu tính toán:
 Tính toán tiền lãi đối với Sổ tiết kiệm không kỳ hạn
 Tính toán tiền lãi đối với sổ tiết kiệm có kỳ hạn
1.2.3. Yêu cầu tra cứu:
 Tra cứu thông tin tài khoản
 Tra cứu thông tin sổ tiết kiệm
 Tra cứu thông tin nhân viên
 Tra cứu nhật ký thao tác tài khoản
 Tra cứu nhật ký thao tác sổ tiết kiệm
1.2.4. Yêu cầu thống kê, tổng hợp:
 Thống kê danh sách sổ tiết kiệm
 Thống kê danh sách tài khoản
 Thống kê danh sách phiếu chi
 Thống kê danh sách phiếu thu
III. Yêu cầu phi chức năng
1.3.1. Yêu cầu bảo mật:
 Mã hóa mật khẩu đăng nhập
 Phân quyền người dùng đăng nhập vào hệ thống:
