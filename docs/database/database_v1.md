//////////////////////////////////////////////////////////
// HoLe The Spirits
// PostgreSQL
// Sprint 2.1 Final
//////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////
// Lookup Tables Product
//////////////////////////////////////////////////////////

Table countries [note: 'Danh sách quốc gia'] {
  id bigint [pk, increment, note: 'Khóa chính']

  code varchar(10) [unique, not null, note: 'Mã quốc gia ISO']

  name varchar(100) [not null, note: 'Tên quốc gia']

  description text [note: 'Mô tả']

  sort_order int [default: 0]

  is_active boolean [default: true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table units [note: 'Đơn vị tính sản phẩm'] {

  id bigint [pk, increment]

  code varchar(20) [unique, not null, note: 'ML, BOTTLE, BOX...']

  name varchar(50) [not null]

  description text

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table image_types [note:'Loại hình ảnh']{

  id bigint [pk, increment]

  code varchar(30) [unique]

  name varchar(50)

  description text

  sort_order int

  is_active boolean

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table product_statuses [note:'Trạng thái sản phẩm']{

  id bigint [pk, increment]

  code varchar(30) [unique]

  name varchar(100)

  description text

  sort_order int

  is_active boolean

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// Master Tables
//////////////////////////////////////////////////////////

Table categories [note:'Danh mục sản phẩm']{

  id bigint [pk, increment]

  parent_id bigint [ref: > categories.id, note:'Danh mục cha']

  code varchar(30) [unique, not null]

  name varchar(100) [not null]

  slug varchar(150) [unique, not null]

  description text

  image_url text

  meta_title varchar(255)

  meta_description text

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table brands [note:'Thương hiệu sản phẩm']{

  id bigint [pk, increment]

  code varchar(30) [unique, not null]

  name varchar(100) [not null]

  slug varchar(150) [unique]

  manufacturer_name varchar(150)

  country_id bigint [ref: > countries.id]

  website varchar(255)

  logo_url text

  description text

  meta_title varchar(255)

  meta_description text

  founded_year smallint

  is_featured boolean [default:false]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table products [note:'Sản phẩm gốc, không lưu giá và tồn kho']{

  id bigint [pk, increment]

  category_id bigint [not null, ref: > categories.id]

  brand_id bigint [not null, ref: > brands.id]

  code varchar(30) [unique, not null]

  name varchar(200) [not null]

  slug varchar(255) [unique]

  short_description text

  description text

  origin_country_id bigint [ref: > countries.id]

  alcohol_percentage numeric(5,2)

  meta_title varchar(255)

  meta_description text

  status_id bigint [ref: > product_statuses.id]

  is_featured boolean [default:false]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table product_variants [note:'SKU thực tế dùng để nhập hàng, bán hàng và quản lý tồn kho']{

  id bigint [pk, increment]

  product_id bigint [not null, ref: > products.id]

  sku varchar(50) [unique, not null]

  barcode varchar(100)

  volume_ml integer

  unit_id bigint [ref: > units.id]

  cost_price numeric(12,2)

  sale_price numeric(12,2)

  compare_price numeric(12,2)

  weight_gram integer

  stock_alert integer [default:0]

  is_track_inventory boolean [default:true]

  is_default boolean [default:false]

  status_id bigint [ref: > product_statuses.id]

  sort_order integer [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table product_images [note:'Hình ảnh theo từng Product Variant']{

  id bigint [pk, increment]

  product_variant_id bigint [ref: > product_variants.id]

  image_url text

  title varchar(255)

  alt_text varchar(255)

  caption text

  image_type_id bigint [ref: > image_types.id]

  display_order smallint [default:0]

  is_thumbnail boolean [default:false]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// HoLe The Spirits
// Sprint 2.2 - Customer Domain
//////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////
// Lookup Tables
//////////////////////////////////////////////////////////

Table genders [note: 'Giới tính khách hàng'] {

  id bigint [pk, increment, note:'Khóa chính']

  code varchar(20) [unique, not null, note:'MALE, FEMALE...']

  name varchar(50) [not null, note:'Tên hiển thị']

  description text [note:'Mô tả']

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table customer_sources [note:'Nguồn khách hàng biết đến cửa hàng'] {

  id bigint [pk, increment]

  code varchar(30) [unique, not null]

  name varchar(100) [not null]

  description text

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table customer_types [note:'Loại khách hàng'] {

  id bigint [pk, increment]

  code varchar(30) [unique, not null]

  name varchar(100) [not null]

  description text

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table contact_platforms [note:'Các nền tảng liên hệ với khách hàng'] {

  id bigint [pk, increment]

  code varchar(30) [unique, not null]

  name varchar(100) [not null]

  description text

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table address_types [note:'Loại địa chỉ'] {

  id bigint [pk, increment]

  code varchar(30) [unique, not null]

  name varchar(100) [not null]

  description text

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// Master Tables Customer
//////////////////////////////////////////////////////////

Table customers [note:'Thông tin khách hàng của hệ thống Retail'] {

  id bigint [pk, increment, note:'Khóa chính']

  customer_code varchar(30) [unique, not null, note:'CUS0000001']

  full_name varchar(200) [not null, note:'Họ tên khách hàng']

  phone varchar(20) [unique, not null, note:'Số điện thoại định danh']

  email varchar(255) [note:'Email (không bắt buộc)']

  birthday date [note:'Ngày sinh']

  gender_id bigint [ref: > genders.id, note:'Giới tính']

  customer_source_id bigint [ref: > customer_sources.id, note:'Nguồn khách hàng']

  customer_type_id bigint [ref: > customer_types.id, note:'Loại khách hàng']

  preferred_contact_platform_id bigint [ref: > contact_platforms.id, note:'Nền tảng liên hệ ưu tiên']

  total_orders integer [default:0, note:'Cache tổng số đơn hàng']

  total_spent numeric(14,2) [default:0, note:'Cache tổng chi tiêu']

  last_order_at timestamp [note:'Ngày đặt đơn gần nhất']

  note text [note:'Ghi chú nội bộ']

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table customer_addresses [note: 'Danh sách địa chỉ của khách hàng'] {

  id bigint [pk, increment]

  customer_id bigint [not null, ref: > customers.id, note:'Khách hàng']

  address_type_id bigint [ref: > address_types.id, note:'Loại địa chỉ']

  receiver_name varchar(200) [not null, note:'Tên người nhận']

  receiver_phone varchar(20) [not null, note:'SĐT người nhận']

  address text [not null, note:'Địa chỉ đầy đủ']

  is_default boolean [default:false, note:'Địa chỉ mặc định']

  note text

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table customer_contacts [note:'Các tài khoản mạng xã hội và kênh liên hệ của khách hàng'] {

  id bigint [pk, increment]

  customer_id bigint [not null, ref: > customers.id]

  contact_platform_id bigint [not null, ref: > contact_platforms.id]

  contact_value varchar(255) [not null, note:'Username, link hoặc số điện thoại']

  is_primary boolean [default:false, note:'Kênh liên hệ chính']

  note text

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// HoLe The Spirits
// Sprint 2.3
// Order Domain
//////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////
// Lookup Tables
//////////////////////////////////////////////////////////

Table order_statuses [note: 'Danh sách trạng thái đơn hàng'] {

  id bigint [pk, increment, note:'Khóa chính']

  code varchar(30) [unique, not null, note:'NEW, CONFIRMED, PREPARING...']

  name varchar(100) [not null, note:'Tên hiển thị']

  description text [note:'Mô tả']

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table order_sources [note: 'Nguồn tạo đơn hàng'] {

  id bigint [pk, increment]

  code varchar(30) [unique, not null]

  name varchar(100) [not null]

  description text

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// Transaction Tables
//////////////////////////////////////////////////////////

Table orders [note: 'Header của đơn hàng'] {

  id bigint [pk, increment, note:'Khóa chính']

  order_no varchar(20) [unique, not null, note:'SO0001, SO0002...']

  customer_id bigint [not null, ref: > customers.id, note:'FK khách hàng']

  order_status_id bigint [not null, ref: > order_statuses.id]

  order_source_id bigint [ref: > order_sources.id]

  ////////////////////////////////////////////////////////
  // Snapshot Customer
  ////////////////////////////////////////////////////////

  customer_name varchar(200) [not null, note:'Tên khách tại thời điểm đặt hàng']

  customer_phone varchar(20) [not null, note:'SĐT tại thời điểm đặt hàng']

  ////////////////////////////////////////////////////////
  // Snapshot Shipping
  ////////////////////////////////////////////////////////

  shipping_receiver_name varchar(200) [not null, note:'Tên người nhận']

  shipping_receiver_phone varchar(20) [not null, note:'SĐT người nhận']

  shipping_address text [not null, note:'Địa chỉ giao hàng đã format']

  ////////////////////////////////////////////////////////
  // Business Dates
  ////////////////////////////////////////////////////////

  order_date timestamp [not null, note:'Ngày tạo đơn']

  delivery_date timestamp [note:'Ngày dự kiến giao']

  ////////////////////////////////////////////////////////
  // Staff
  ////////////////////////////////////////////////////////

  sale_staff_id bigint [ref: > staffs.id, note:'Nhân viên bán hàng']
  delivery_staff_id bigint [ref: > staffs.id, note:'Nhân viên giao hàng']
  cash_collector_staff_id bigint [ref: > staffs.id, note:'Nhân viên thu tiền']

  ////////////////////////////////////////////////////////
  // Amount
  ////////////////////////////////////////////////////////

  product_subtotal numeric(14,2) [default:0, note:'Tổng tiền hàng trước giảm giá']

  discount_amount numeric(14,2) [default:0, note:'Tổng tiền giảm giá']

  product_total numeric(14,2) [default:0, note:'Tổng tiền hàng sau giảm giá, chưa gồm phí ship']

  shipping_fee numeric(14,2) [default:0, note:'Phí giao hàng']

  order_total numeric(14,2) [default:0, note:'Tổng khách phải thanh toán, đã gồm phí ship']

  ////////////////////////////////////////////////////////
  // Note
  ////////////////////////////////////////////////////////

  customer_note text [note:'Ghi chú từ khách']

  internal_note text [note:'Ghi chú nội bộ']

  ////////////////////////////////////////////////////////

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table order_items [note: 'Chi tiết sản phẩm của đơn hàng'] {

  id bigint [pk, increment]

  order_id bigint [not null, ref: > orders.id]

  product_variant_id bigint [not null, ref: > product_variants.id]

  ////////////////////////////////////////////////////////
  // Snapshot Product
  ////////////////////////////////////////////////////////

  sku_snapshot varchar(100) [not null, note:'SKU tại thời điểm bán']

  product_name_snapshot varchar(255) [not null, note:'Tên sản phẩm tại thời điểm bán']

  ////////////////////////////////////////////////////////

  quantity numeric(10,2) [not null, note:'Số lượng']

  unit_price numeric(14,2) [not null, note:'Đơn giá']

  discount_amount numeric(14,2) [default:0, note:'Giảm giá dòng sản phẩm']

  subtotal numeric(14,2) [not null, note:'Thành tiền']

  note text

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// HoLe The Spirits
// Sprint 2.4
// Inventory Management
//////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////
// Lookup Tables
//////////////////////////////////////////////////////////

Table inventory_transaction_types [note: 'Loại giao dịch kho'] {

  id bigint [pk, increment]

  code varchar(30) [unique, not null, note:'PURCHASE, SALE, TRANSFER, ADJUSTMENT...']

  name varchar(100) [not null]

  description text

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// Master Tables
//////////////////////////////////////////////////////////

Table warehouses [note: 'Danh sách kho hàng'] {

  id bigint [pk, increment]

  warehouse_code varchar(20) [unique, not null, note:'WH001']

  warehouse_name varchar(200) [not null, note:'HoLe An Bình']

  manager_staff_id bigint [ref: > staffs.id, note:'Quản lý kho']

  phone varchar(20)

  address text

  description text

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// Current Inventory
//////////////////////////////////////////////////////////

Table warehouse_inventory [note: 'Tồn kho hiện tại của từng sản phẩm theo từng kho'] {

  id bigint [pk, increment]

  warehouse_id bigint [not null, ref: > warehouses.id]

  product_variant_id bigint [not null, ref: > product_variants.id]

  quantity numeric(12,2) [default:0, note:'Số lượng tồn hiện tại']

  updated_at timestamp

  Note: 'Unique (warehouse_id, product_variant_id)'
}

//////////////////////////////////////////////////////////
// Inventory Ledger
//////////////////////////////////////////////////////////

Table inventory_transactions [note: 'Sổ cái kho - Hệ thống tự sinh'] {

  id bigint [pk, increment]

  transaction_no varchar(30) [unique, not null, note:'IT000001']

  inventory_transaction_type_id bigint [not null, ref: > inventory_transaction_types.id]

  reference_type varchar(30) [not null, note:'ORDER, PURCHASE, TRANSFER']

  reference_id bigint [not null, note:'ID của chứng từ gốc']

  transaction_date timestamp [not null]

  note text

  created_at timestamp
  created_by bigint
}

Table inventory_movements {

  id bigint [pk, increment]

  code varchar(10) [unique, not null] // IN, OUT

  name varchar(50) [not null]

  description text

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table inventory_transaction_items [note: 'Chi tiết biến động tồn kho'] {

  id bigint [pk, increment]

  inventory_transaction_id bigint [not null, ref: > inventory_transactions.id]

  warehouse_id bigint [not null, ref: > warehouses.id]

  product_variant_id bigint [not null, ref: > product_variants.id]

  quantity numeric(12,2) [not null, note:'Luôn là số dương']

  inventory_movement_id bigint [not null, ref: > inventory_movements.id]

  note text

  created_at timestamp
  created_by bigint
}

//////////////////////////////////////////////////////////
// HoLe The Spirits
// Sprint 2.5
// Purchase Domain
//////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////
// Lookup Tables
//////////////////////////////////////////////////////////

Table supplier_types [note: 'Phân loại nhà cung cấp'] {

  id bigint [pk, increment]

  code varchar(30) [unique, not null]

  name varchar(100) [not null]

  description text

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table purchase_statuses [note: 'Trạng thái phiếu nhập'] {

  id bigint [pk, increment]

  code varchar(30) [unique, not null]

  name varchar(100) [not null]

  description text

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// Master
//////////////////////////////////////////////////////////

Table suppliers [note: 'Nhà cung cấp'] {

  id bigint [pk, increment]

  supplier_code varchar(20) [unique, not null, note:'SUP0001']

  supplier_name varchar(255) [not null]

  supplier_type_id bigint [ref: > supplier_types.id]

  contact_name varchar(200)

  phone varchar(20)

  email varchar(255)

  address text

  tax_code varchar(50)

  note text

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// Purchase Header
//////////////////////////////////////////////////////////

Table purchases [note: 'Phiếu nhập hàng'] {

  id bigint [pk, increment]

  purchase_no varchar(20) [unique, not null, note:'PO0001']

  supplier_id bigint [not null, ref: > suppliers.id]

  warehouse_id bigint [not null, ref: > warehouses.id]
  
  purchase_staff_id bigint [ref: > staffs.id, note:'Nhân viên nhập hàng']

  purchase_status_id bigint [not null, ref: > purchase_statuses.id]

  inventory_transaction_id bigint [ref: > inventory_transactions.id, note:'Ledger được hệ thống tự sinh']

  ////////////////////////////////////////////////////////
  // Snapshot
  ////////////////////////////////////////////////////////

  supplier_name_snapshot varchar(255) [not null]

  warehouse_name_snapshot varchar(255) [not null]

  ////////////////////////////////////////////////////////

  purchase_date timestamp [not null]

  received_date timestamp

  ////////////////////////////////////////////////////////

  total_amount numeric(14,2) [default:0]

  note text

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// Purchase Detail
//////////////////////////////////////////////////////////

Table purchase_items [note: 'Chi tiết phiếu nhập'] {

  id bigint [pk, increment]

  purchase_id bigint [not null, ref: > purchases.id]

  product_variant_id bigint [not null, ref: > product_variants.id]

  ////////////////////////////////////////////////////////
  // Snapshot
  ////////////////////////////////////////////////////////

  sku_snapshot varchar(100) [not null]

  product_name_snapshot varchar(255) [not null]

  ////////////////////////////////////////////////////////

  quantity numeric(12,2) [not null]

  unit_cost numeric(14,2) [not null]

  subtotal numeric(14,2) [not null]

  note text

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// HoLe The Spirits
// Sprint 2.6
// Combo & Bundle
//////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////
// Lookup Tables
//////////////////////////////////////////////////////////

Table product_types [note: 'Phân loại sản phẩm'] {

  id bigint [pk, increment]

  code varchar(30) [unique, not null, note:'NORMAL, COMBO, GIFT_BOX, ACCESSORY']

  name varchar(100) [not null]

  description text

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// Combo Components
//////////////////////////////////////////////////////////

Table combo_items [note: 'Danh sách thành phần của Combo'] {

  id bigint [pk, increment]

  combo_variant_id bigint [not null, ref: > product_variants.id, note:'Variant của Combo']

  component_variant_id bigint [not null, ref: > product_variants.id, note:'Variant thành phần']

  quantity numeric(12,2) [not null, default:1, note:'Số lượng thành phần']

  ////////////////////////////////////////////////////////
  // Cost Snapshot
  ////////////////////////////////////////////////////////

  default_unit_cost numeric(14,2) [default:0, note:'Giá vốn mặc định tại thời điểm cấu hình combo']

  ////////////////////////////////////////////////////////

  is_required boolean [default:true, note:'Có bắt buộc trong combo hay không']

  display_order int [default:1, note:'Thứ tự hiển thị']

  effective_from timestamp [note:'Ngày bắt đầu hiệu lực']

  effective_to timestamp [note:'Ngày kết thúc hiệu lực']

  note text

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint

  Note: '''
  Unique(combo_variant_id, component_variant_id)

  Inventory không quản lý Combo.
  Inventory chỉ quản lý component_variant_id.

  Khi Order chuyển sang SHIPPING:

      Combo
          ↓
      Inventory Engine
          ↓
      Đọc combo_items
          ↓
      Sinh Inventory Transactions
          ↓
      Trừ tồn từng component.
  '''
}

//////////////////////////////////////////////////////////
// HoLe The Spirits
// Sprint 2.7
// Warehouse Transfer
//////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////
// Lookup Tables
//////////////////////////////////////////////////////////

Table transfer_statuses [note: 'Trạng thái phiếu chuyển kho'] {

  id bigint [pk, increment]

  code varchar(30) [unique, not null]

  name varchar(100) [not null]

  description text

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

Table transfer_reasons [note: 'Lý do chuyển kho'] {

  id bigint [pk, increment]

  code varchar(30) [unique, not null]

  name varchar(100) [not null]

  description text

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// Transfer Header
//////////////////////////////////////////////////////////

Table transfers [note: 'Phiếu chuyển kho'] {

  id bigint [pk, increment]

  transfer_no varchar(20) [unique, not null, note:'TF0001']

  source_warehouse_id bigint [not null, ref: > warehouses.id]

  destination_warehouse_id bigint [not null, ref: > warehouses.id]

  transfer_staff_id bigint [ref: > staffs.id, note:'Nhân viên chuyển kho']
  
  received_staff_id bigint [ref: > staffs.id, note:'Nhân viên nhận kho']

  transfer_reason_id bigint [ref: > transfer_reasons.id]

  transfer_status_id bigint [not null, ref: > transfer_statuses.id]

  inventory_transaction_id bigint [ref: > inventory_transactions.id, note:'Ledger tự sinh']

  ////////////////////////////////////////////////////////
  // Snapshot
  ////////////////////////////////////////////////////////

  source_warehouse_snapshot varchar(255)

  destination_warehouse_snapshot varchar(255)

  ////////////////////////////////////////////////////////

  transfer_date timestamp [not null]

  note text

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// Transfer Detail
//////////////////////////////////////////////////////////

Table transfer_items [note: 'Chi tiết phiếu chuyển kho'] {

  id bigint [pk, increment]

  transfer_id bigint [not null, ref: > transfers.id]

  product_variant_id bigint [not null, ref: > product_variants.id]

  ////////////////////////////////////////////////////////
  // Snapshot
  ////////////////////////////////////////////////////////

  sku_snapshot varchar(100)

  product_name_snapshot varchar(255)

  ////////////////////////////////////////////////////////

  quantity numeric(12,2) [not null]

  note text

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// HoLe The Spirits
// Sprint 2.8
// Stock Adjustment
//////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////
// Lookup Tables
//////////////////////////////////////////////////////////

Table adjustment_reasons [note: 'Lý do điều chỉnh tồn kho'] {

  id bigint [pk, increment]

  code varchar(30) [unique, not null]

  name varchar(100) [not null]

  description text

  sort_order int [default:0]

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// Adjustment Header
//////////////////////////////////////////////////////////

Table stock_adjustments [note: 'Phiếu điều chỉnh tồn kho'] {

  id bigint [pk, increment]

  adjustment_no varchar(20) [unique, not null, note:'SA0001']

  warehouse_id bigint [not null, ref: > warehouses.id]

  adjustment_staff_id bigint [ref: > staffs.id, note:'Nhân viên điều chỉnh tồn kho']

  adjustment_reason_id bigint [not null, ref: > adjustment_reasons.id]

  inventory_transaction_id bigint [ref: > inventory_transactions.id, note:'Ledger tự sinh']

  adjustment_date timestamp [not null]

  note text

  is_active boolean [default:true]

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// Adjustment Detail
//////////////////////////////////////////////////////////

Table stock_adjustment_items [note: 'Chi tiết điều chỉnh tồn kho'] {

  id bigint [pk, increment]

  stock_adjustment_id bigint [not null, ref: > stock_adjustments.id]

  product_variant_id bigint [not null, ref: > product_variants.id]

  ////////////////////////////////////////////////////////
  // Snapshot
  ////////////////////////////////////////////////////////

  sku_snapshot varchar(100)

  product_name_snapshot varchar(255)

  ////////////////////////////////////////////////////////

  system_quantity numeric(12,2) [not null, note:'Số lượng theo hệ thống']

  actual_quantity numeric(12,2) [not null, note:'Số lượng kiểm thực tế']

  adjustment_quantity numeric(12,2) [not null, note:'Actual - System']

  note text

  created_at timestamp
  created_by bigint

  updated_at timestamp
  updated_by bigint

  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// HoLe The Spirits
// Phase 3 - Sprint 3.1
// Staff Management
//////////////////////////////////////////////////////////

Table staff_positions [note: 'Chức vụ nhân viên'] {
  id bigint [pk, increment]
  code varchar(30) [unique, not null, note:'OWNER, SALES, WAREHOUSE, DELIVERY, ADMIN']
  name varchar(100) [not null, note:'Tên chức vụ']
  description text
  sort_order int [default:0]
  is_active boolean [default:true]
  created_at timestamp
  created_by bigint
  updated_at timestamp
  updated_by bigint
  deleted_at timestamp
  deleted_by bigint
}

Table staff_types [note: 'Loại nhân viên'] {
  id bigint [pk, increment]
  code varchar(30) [unique, not null, note:'FULLTIME, PARTTIME, FREELANCER']
  name varchar(100) [not null]
  description text
  sort_order int [default:0]
  is_active boolean [default:true]
  created_at timestamp
  created_by bigint
  updated_at timestamp
  updated_by bigint
  deleted_at timestamp
  deleted_by bigint
}

Table staff_statuses [note: 'Trạng thái nhân viên'] {
  id bigint [pk, increment]
  code varchar(30) [unique, not null, note:'ACTIVE, INACTIVE, RESIGNED, ON_LEAVE']
  name varchar(100) [not null]
  description text
  sort_order int [default:0]
  is_active boolean [default:true]
  created_at timestamp
  created_by bigint
  updated_at timestamp
  updated_by bigint
  deleted_at timestamp
  deleted_by bigint
}

Table staffs [note: 'Thông tin nhân viên'] {
  id bigint [pk, increment]
  staff_code varchar(20) [unique, not null, note:'EMP0001']
  full_name varchar(255) [not null, note:'Họ và tên']
  phone varchar(20) [note:'Số điện thoại']
  email varchar(255) [note:'Email']
  staff_position_id bigint [not null, ref: > staff_positions.id, note:'Chức vụ']
  staff_type_id bigint [not null, ref: > staff_types.id, note:'Loại nhân viên']
  staff_status_id bigint [not null, ref: > staff_statuses.id, note:'Trạng thái']
  default_warehouse_id bigint [ref: > warehouses.id, note:'Kho mặc định']
  hire_date date [note:'Ngày vào làm']
  avatar_url varchar(500) [note:'Ảnh đại diện']
  note text
  is_active boolean [default:true]
  created_at timestamp
  created_by bigint
  updated_at timestamp
  updated_by bigint
  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// HoLe The Spirits
// Phase 3 - Sprint 3.2
// User Authentication
//////////////////////////////////////////////////////////

Table user_statuses [note: 'Trạng thái tài khoản'] {
  id bigint [pk, increment]
  code varchar(30) [unique, not null, note:'ACTIVE, LOCKED, DISABLED, PENDING']
  name varchar(100) [not null]
  description text
  sort_order int [default:0]
  is_active boolean [default:true]
  created_at timestamp
  created_by bigint
  updated_at timestamp
  updated_by bigint
  deleted_at timestamp
  deleted_by bigint
}

Table users [note: 'Tài khoản đăng nhập hệ thống'] {
  id bigint [pk, increment]
  username varchar(100) [unique, not null, note:'Tên đăng nhập']
  password_hash varchar(255) [not null, note:'Mật khẩu đã mã hóa']
  staff_id bigint [unique, not null, ref: > staffs.id, note:'Liên kết nhân viên']
  user_status_id bigint [not null, ref: > user_statuses.id, note:'Trạng thái tài khoản']
  last_login_at timestamp [note:'Lần đăng nhập gần nhất']
  last_login_ip varchar(50) [note:'IP đăng nhập gần nhất']
  failed_login_attempt int [default:0, note:'Số lần đăng nhập sai liên tiếp']
  locked_until timestamp [note:'Khóa đến thời điểm']
  must_change_password boolean [default:false, note:'Bắt buộc đổi mật khẩu']
  is_active boolean [default:true]
  created_at timestamp
  created_by bigint
  updated_at timestamp
  updated_by bigint
  deleted_at timestamp
  deleted_by bigint
}

Table login_histories [note: 'Lịch sử đăng nhập'] {
  id bigint [pk, increment]
  user_id bigint [not null, ref: > users.id]
  login_at timestamp [not null]
  ip_address varchar(50) [note:'Địa chỉ IP']
  user_agent varchar(500) [note:'Thiết bị hoặc trình duyệt']
  is_success boolean [not null, note:'Đăng nhập thành công hay thất bại']
  failure_reason varchar(255) [note:'Lý do thất bại nếu có']
  created_at timestamp
}

//////////////////////////////////////////////////////////
// HoLe The Spirits
// Phase 3 - Sprint 3.3
// Business Modules (RBAC Extension)
//////////////////////////////////////////////////////////

Table system_modules [note: 'Danh mục module nghiệp vụ'] {
  id bigint [pk, increment]
  code varchar(50) [unique, not null, note:'PRODUCT, CUSTOMER, ORDER, PURCHASE, WAREHOUSE, TRANSFER...']
  name varchar(100) [not null, note:'Tên module']
  description text
  sort_order int [default:0]
  icon varchar(100) [note:'Tên icon hiển thị']
  route varchar(255) [note:'Đường dẫn frontend']
  is_active boolean [default:true]
  created_at timestamp
  created_by bigint
  updated_at timestamp
  updated_by bigint
  deleted_at timestamp
  deleted_by bigint
}

//////////////////////////////////////////////////////////
// HoLe The Spirits
// Phase 3 - Sprint 3.4
// Audit Log
//////////////////////////////////////////////////////////

Table audit_logs [note: 'Nhật ký thay đổi dữ liệu'] {
  id bigint [pk, increment]
  module_code varchar(50) [not null, note:'ORDER, PRODUCT, CUSTOMER...']
  entity_name varchar(100) [not null, note:'Tên bảng']
  entity_id bigint [not null, note:'ID bản ghi']
  action varchar(20) [not null, note:'CREATE, UPDATE, DELETE']
  changed_by bigint [not null, ref: > users.id, note:'Người thực hiện']
  ip_address varchar(50) [note:'Địa chỉ IP']
  user_agent varchar(500) [note:'Thiết bị hoặc trình duyệt']
  old_data jsonb [note:'Dữ liệu trước khi thay đổi']
  new_data jsonb [note:'Dữ liệu sau khi thay đổi']
  changed_at timestamp [not null]
}

//////////////////////////////////////////////////////////
// HoLe The Spirits
// Phase 3 - Sprint 3.5
// System Settings
//////////////////////////////////////////////////////////

Table setting_groups [note: 'Nhóm cấu hình hệ thống'] {
  id bigint [pk, increment]
  code varchar(50) [unique, not null, note:'GENERAL, BUSINESS, INVENTORY, DOCUMENT, INTEGRATION']
  name varchar(100) [not null]
  description text
  sort_order int [default:0]
  is_active boolean [default:true]
  created_at timestamp
  created_by bigint
  updated_at timestamp
  updated_by bigint
  deleted_at timestamp
  deleted_by bigint
}

Table system_settings [note: 'Cấu hình hệ thống dạng Key-Value'] {
  id bigint [pk, increment]
  setting_group_id bigint [not null, ref: > setting_groups.id]
  setting_key varchar(100) [unique, not null, note:'SHOP_NAME, ORDER_PREFIX...']
  setting_name varchar(255) [not null, note:'Tên hiển thị']
  setting_value text [note:'Giá trị cấu hình']
  data_type varchar(30) [not null, note:'STRING, INTEGER, BOOLEAN, JSON']
  description text
  is_system boolean [default:false, note:'Không cho phép xóa']
  is_editable boolean [default:true, note:'Cho phép chỉnh sửa trên UI']
  sort_order int [default:0]
  is_active boolean [default:true]
  created_at timestamp
  created_by bigint
  updated_at timestamp
  updated_by bigint
  deleted_at timestamp
  deleted_by bigint
}