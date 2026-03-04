"""
电商智能客服 - 订单 API 集成示例
演示如何与电商订单系统进行 API 集成
"""

import requests
import json
from typing import Dict, Optional


class OrderAPIClient:
    """订单 API 客户端"""
    
    def __init__(self, base_url: str, api_key: str):
        """
        初始化订单 API 客户端
        
        Args:
            base_url: API 基础 URL
            api_key: API 密钥
        """
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        })
    
    def get_order_info(self, order_id: str) -> Optional[Dict]:
        """
        获取订单详细信息
        
        Args:
            order_id: 订单号
            
        Returns:
            订单信息字典，如果不存在则返回 None
        """
        try:
            response = self.session.get(
                f'{self.base_url}/orders/{order_id}',
                timeout=5
            )
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print(f"订单 {order_id} 不存在")
                return None
            else:
                print(f"查询订单失败：{response.status_code}")
                return None
                
        except requests.RequestException as e:
            print(f"API 请求异常：{e}")
            return None
    
    def validate_order_for_return(self, order_id: str) -> Dict:
        """
        验证订单是否可以退货
        
        Args:
            order_id: 订单号
            
        Returns:
            验证结果：{'valid': bool, 'reason': str}
        """
        order_info = self.get_order_info(order_id)
        
        if not order_info:
            return {'valid': False, 'reason': '订单不存在'}
        
        # 检查退货条件
        if order_info.get('status') not in ['completed', 'delivered']:
            return {'valid': False, 'reason': '订单未完成，无法退货'}
        
        # 检查是否在 7 天无理由退货期内
        from datetime import datetime, timedelta
        delivery_date = datetime.fromisoformat(order_info.get('delivery_date', ''))
        if datetime.now() - delivery_date > timedelta(days=7):
            return {'valid': False, 'reason': '已超过 7 天无理由退货期'}
        
        # 检查是否为特殊商品
        if order_info.get('is_special_product', False):
            return {'valid': False, 'reason': '特殊商品不支持无理由退货'}
        
        return {'valid': True, 'reason': '符合退货条件'}
    
    def create_return_request(self, order_data: Dict) -> Optional[str]:
        """
        创建退货申请
        
        Args:
            order_data: 订单数据，包含 order_id, return_reason, return_method
            
        Returns:
            退货申请 ID，失败返回 None
        """
        try:
            response = self.session.post(
                f'{self.base_url}/returns',
                json=order_data,
                timeout=5
            )
            
            if response.status_code == 201:
                result = response.json()
                return result.get('return_id')
            else:
                print(f"创建退货申请失败：{response.status_code}")
                return None
                
        except requests.RequestException as e:
            print(f"API 请求异常：{e}")
            return None
    
    def get_order_status(self, order_id: str) -> Optional[str]:
        """
        获取订单状态
        
        Args:
            order_id: 订单号
            
        Returns:
            订单状态文本
        """
        order_info = self.get_order_info(order_id)
        if order_info:
            return order_info.get('status', 'unknown')
        return None


# 演示代码
if __name__ == '__main__':
    # 初始化客户端（使用示例配置）
    client = OrderAPIClient(
        base_url='https://api.example-ecommerce.com',
        api_key='your_api_key_here'
    )
    
    # 示例 1: 查询订单信息
    print("=== 查询订单信息 ===")
    order_id = 'ABC12345678'
    order_info = client.get_order_info(order_id)
    if order_info:
        print(json.dumps(order_info, indent=2, ensure_ascii=False))
    
    # 示例 2: 验证订单是否可退货
    print("\n=== 验证退货资格 ===")
    validation = client.validate_order_for_return(order_id)
    print(f"验证结果：{validation}")
    
    # 示例 3: 创建退货申请
    print("\n=== 创建退货申请 ===")
    return_data = {
        'order_id': order_id,
        'return_reason': '商品质量问题',
        'return_method': '上门取件'
    }
    return_id = client.create_return_request(return_data)
    if return_id:
        print(f"退货申请创建成功，退货编号：{return_id}")
