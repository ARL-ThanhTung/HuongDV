from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from app.db.base import SessionLocal, engine
from app.router.router import router
#from app.models.Base.metadata.create_all(bind=engine)
from fastapi.responses import ORJSONResponse
from app.db.base import get_db
from app.model.base import Base
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine, checkfirst=True) 

app = FastAPI(title="Phát triển phần mềm hướng dịch vụ",
        docs_url='/docs',
        # docs_url=None,
        redoc_url=None,
        openapi_url=f"/openapi.json",
        description='''PROJECTS''',)



@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_json():
    return app.openapi()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả các origin (cần được điều chỉnh tùy theo yêu cầu cụ thể)
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép tất cả các phương thức
    allow_headers=["*"],  # Cho phép tất cả các tiêu đề
)

@app.get("/open" , response_class=ORJSONResponse)
async def get_openapi_json():
    return ORJSONResponse([{"item_id": "Foo"}])

app.include_router(router, prefix="/app")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000, debug=False, reload=False, workers=4)



# {
#   "title": "Asus TUF Gaming FX506HF-HN017W i5 11400H/16GB/512GB/GeForce RTX 2050 4GB/Win11",
#   "image": "https://images.fpt.shop/unsafe/fit-in/filters:quality(90):fill(white):upscale()/fptshop.com.vn/Uploads/Originals/2023/4/4/638162268369378408_asus-tuf-gaming-fx506hf-den-1.jpg",
#   "description": "ASUS TUF Gaming F15 FX506HF HN017W là chiếc laptop gaming giá rẻ nhưng vô cùng mạnh mẽ. Không chỉ bộ vi xử lý Intel thế hệ thứ 11, card đồ họa RTX 20 series mà điểm mạnh còn đến từ việc trang bị sẵn 16GB RAM, cho bạn hiệu năng xuất sắc mà không cần nâng cấp máy",
#   "category_id": 3,
#   "branch_id": 7,
#   "product_detail": [
#     {
#       "ram": "8",
#       "rom": "512",
#       "os": "Window ",
#       "image": "https://images.fpt.shop/unsafe/filters:quality(90)/fptshop.com.vn/Uploads/images/2015/0511/ASUS-TUF-Gaming-F15-2021-black-fpt-1.jpg",
#       "description": "ASUS TUF Dash F15 2023 trang bị bộ vi xử lý Intel Core i5 11400H thuộc thế hệ thứ 11 Tiger Lake. Con chip này có sức mạnh cực khủng khi sở hữu tới 6 lõi 12 luồng, tốc độ tối đa lên đến 4.50GHz, TDP 45W. Cả hiệu năng đơn nhân và đa nhân đều xuất sắc khiến cho TUF Gaming FX506 không chỉ chơi tốt mọi tựa game hiện nay mà còn làm việc vô cùng hiệu quả khi chạy được cả những phần mềm chuyên nghiệp. Hơn nữa, ASUS TUF Gaming F15 FX506HF HN017W còn có sẵn 16GB RAM, nâng cao hiệu suất và tăng khả năng tương thích game. Ngoài ra, ổ cứng SSD NVMe PCIe dung lượng cao 512GB giúp bạn tải game và mở ứng dụng hết sức nhanh chóng, không cần phải chờ đợi",
#       "camera": "8MP",
#       "camera_self": "8MP",
#       "battery": 3,
#       "card": "NVIDIA Geforce RTX 2050",
#       "video": "https://youtu.be/4KF7cqwTQ9M",
#       "chip": "Core i5, 11400H",
#       "screen": "Full HD",
#       "price": 19900000,
#       "quantity_remain": 50
#     }
#   ]
# }


# {
#   "title": "Asus Vivobook Flip TN3402YA-LZ188W R5-7530U/16GB/512GB/14 Touch/Win11",
#   "image": "https://images.fpt.shop/unsafe/fit-in/filters:quality(90):fill(white):upscale()/fptshop.com.vn/Uploads/Originals/2023/3/24/638152764193437366_asus-vivobook-flip-tn3402y-bac-1.jpg",
#   "description": "ASUS Vivobook Flip TN3402YA-LZ188W sẽ cùng bạn làm chủ cuộc chơi với khả năng xoay gập mượt mà, màn hình cảm ứng cực nhạy và hiệu suất ấn tượng của bộ vi xử lý Ryzen 5 7000 series. Đây là lựa chọn hoàn hảo cho công việc và giải trí hàng ngày, cho bạn sáng tạo không giới hạn, đạt năng suất làm việc tối đa",
#   "category_id": 2,
#   "branch_id": 7,
#   "product_detail": [
#     {
#       "ram": "8",
#       "rom": "512",
#       "os": "Window 11",
#       "image": "https://images.fpt.shop/unsafe/filters:quality(90)/fptshop.com.vn/Uploads/images/2015/0511/ASUS-Vivobook-S-14-Flip-TN3402-10.jpg",
#       "description": "Không có gì phải nghi ngờ về sức mạnh của ASUS Vivobook S 14 Flip TN3402, chiếc laptop này trang bị bộ vi xử lý AMD Ryzen 5 7530U, con chip thuộc thế hệ 7000 series mới nhất từ nhà AMD, với 6 nhân 12 luồng và tốc độ tối đa lên tới 4.5 GHz. Bên cạnh đó máy còn có tới 16GB RAM, thoải mái cho hoạt động đa nhiệm. Kết quả là mọi tác vụ tính toán hàng ngày của bạn đều diễn ra trong chớp mắt, giúp công việc trở nên dễ dàng và thuận tiện hơn",
#       "camera": "8MP",
#       "camera_self": "8MP",
#       "battery": 3,
#       "card": "",
#       "video": "https://youtu.be/xB4-b8xqn5Y",
#       "chip": "Ryzen 5, 7530U",
#       "screen": "Full HD",
#       "price": 15900000,
#       "quantity_remain": 50
#     }
#   ]
# }
    
# {
#   "title": "HP Pavilion 14-dv2073TU i5 1235U/16GB/512GB/Win11",
#   "image": "https://images.fpt.shop/unsafe/fit-in/filters:quality(90):fill(white):upscale()/fptshop.com.vn/Uploads/Originals/2023/4/11/638168307037428356_hp-pavilion-14-dv2073tu-i5-1235u-vang-4.jpg",
#   "description": "Dù có thiết kế nhỏ gọn với màn hình 14 inch, HP Pavilion 14-dv2073TU vẫn tự tin giải quyết tốt các nhu cầu sử dụng hàng ngày của bạn vì máy có hệ thống phần cứng mạnh mẽ. Đồng thời, bạn còn có thể cho máy vào balo hoặc túi đựng và mang đi bất kì nơi nào",
#   "category_id": 2,
#   "branch_id": 8,
#   "product_detail": [
#     {
#       "ram": "16",
#       "rom": "512",
#       "os": "Window 11",
#       "image": "https://images.fpt.shop/unsafe/filters:quality(90)/fptshop.com.vn/Uploads/images/2015/0511/ASUS-Vivobook-S-14-Flip-TN3402-10.jpg",
#       "description": "Không có gì phải nghi ngờ về sức mạnh của ASUS Vivobook S 14 Flip TN3402, chiếc laptop này trang bị bộ vi xử lý AMD Ryzen 5 7530U, con chip thuộc thế hệ 7000 series mới nhất từ nhà AMD, với 6 nhân 12 luồng và tốc độ tối đa lên tới 4.5 GHz. Bên cạnh đó máy còn có tới 16GB RAM, thoải mái cho hoạt động đa nhiệm. Kết quả là mọi tác vụ tính toán hàng ngày của bạn đều diễn ra trong chớp mắt, giúp công việc trở nên dễ dàng và thuận tiện hơn",
#       "camera": "8MP",
#       "camera_self": "8MP",
#       "battery": 3,
#       "card": "",
#       "video": "https://youtu.be/xB4-b8xqn5Y",
#       "chip": "Core i5, 1235U",
#       "screen": "Full HD",
#       "price": 17490000,
#       "quantity_remain": 50
#     }
#   ]
# }