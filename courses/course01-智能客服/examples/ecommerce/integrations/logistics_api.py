"""
电商智能客服 - 物流 API 集成示例
演示如何与物流查询系统进行 API 集成
"""

import requests
import json
from typing import Dict, Optional, List


class LogisticsAPIClient:
    """物流 API 客户端"""
    
    def __init__(self, base_url: str, api_key: str):
        """
        初始化物流 API 客户端
        
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
    
    def get_logistics_info(self, order_id: str) -> Optional[Dict]:
        """
        获取订单物流信息
        
        Args:
            order_id: 订单号
            
        Returns:
            物流信息字典
        """
        try:
            # 先获取订单的物流单号
            order_url = f'{self.base_url}/orders/{order_id}'
            order_response = self.session.get(order_url, timeout=5)
            
            if order_response.status_code != 200:
                print(f"获取订单信息失败：{order_response.status_code}")
                return None
            
            order_data = order_response.json()
            tracking_number = order_data.get('tracking_number')
            
            if not tracking_number:
                print("该订单暂无物流信息")
                return None
            
            # 查询物流轨迹
            logistics_url = f'{self.base_url}/logistics/{tracking_number}'
            logistics_response = self.session.get(logistics_url, timeout=5)
            
            if logistics_response.status_code == 200:
                return logistics_response.json()
            else:
                print(f"查询物流失败：{logistics_response.status_code}")
                return None
                
        except requests.RequestException as e:
            print(f"API 请求异常：{e}")
            return None
    
    def get_logistics_by_tracking_number(self, tracking_number: str, 
                                         express_company: str = None) -> Optional[Dict]:
        """
        根据运单号查询物流信息
        
        Args:
            tracking_number: 运单号
            express_company: 快递公司编码（可选）
            
        Returns:
            物流信息字典
        """
        try:
            params = {'tracking_number': tracking_number}
            if express_company:
                params['express_company'] = express_company
            
            response = self.session.get(
                f'{self.base_url}/logistics/track',
                params=params,
                timeout=5
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"查询物流失败：{response.status_code}")
                return None
                
        except requests.RequestException as e:
            print(f"API 请求异常：{e}")
            return None
    
    def get_supported_express_companies(self) -> List[Dict]:
        """
        获取支持的快递公司列表
        
        Returns:
            快递公司列表
        """
        try:
            response = self.session.get(
                f'{self.base_url}/logistics/companies',
                timeout=5
            )
            
            if response.status_code == 200:
                return response.json().get('companies', [])
            else:
                print(f"获取快递公司列表失败：{response.status_code}")
                return []
                
        except requests.RequestException as e:
            print(f"API 请求异常：{e}")
            return []
    
    def subscribe_logistics_update(self, order_id: str, callback_url: str) -> bool:
        """
        订阅物流更新通知
        
        Args:
            order_id: 订单号
            callback_url: 回调 URL
            
        Returns:
            是否订阅成功
        """
        try:
            response = self.session.post(
                f'{self.base_url}/logistics/subscribe',
                json={
                    'order_id': order_id,
                    'callback_url': callback_url
                },
                timeout=5
            )
            
            if response.status_code == 200:
                print(f"已订阅订单 {order_id} 的物流更新通知")
                return True
            else:
                print(f"订阅物流更新失败：{response.status_code}")
                return False
                
        except requests.RequestException as e:
            print(f"API 请求异常：{e}")
            return False


# 演示代码
if __name__ == '__main__':
    # 初始化客户端（使用示例配置）
    client = LogisticsAPIClient(
        base_url='https://api.example-logistics.com',
        api_key='your_api_key_here'
    )
    
    # 示例 1: 查询订单物流信息
    print("=== 查询订单物流信息 ===")
    order_id = 'ABC12345678'
    logistics_info = client.get_logistics_info(order_id)
    if logistics_info:
        print(json.dumps(logistics_info, indent=2, ensure_ascii=False))
    
    # 示例 2: 根据运单号查询
    print("\n=== 根据运单号查询 ===")
    tracking_number = 'SF1234567890'
    logistics = client.get_logistics_by_tracking_number(tracking_number, 'sf')
    if logistics:
        print(f"快递公司：{logistics.get('express_company')}")
        print(f"当前状态：{logistics.get('current_status')}")
        print("\n物流轨迹:")
        for track in logistics.get('tracks', [])[:3]:
            print(f"  {track.get('time')}: {track.get('desc')}")
    
    # 示例 3: 获取支持的快递公司
    print("\n=== 支持的快递公司 ===")
    companies = client.get_supported_express_companies()
    for company in companies[:5]:
        print(f"  {company.get('name')} ({company.get('code')})")
    
    # 示例 4: 订阅物流更新
    print("\n=== 订阅物流更新 ===")
    success = client.subscribe_logistics_update(
        order_id=order_id,
        callback_url='https://your-domain.com/api/logistics/callback'
    )
    if success:
        print("订阅成功，物流更新时会收到通知")
