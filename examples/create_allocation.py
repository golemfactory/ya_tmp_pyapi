import asyncio
import os

import ya_payment

from ya_payment import ApiClient as PaymentApiClient
from ya_payment.models import Allocation
from ya_payment.api.requestor_api import RequestorApi


def prepare_api():
    app_key = os.getenv("YAGNA_APPKEY")
    if app_key is None:
        raise ValueError("YAGNA_APPKEY environment variable is not set")

    cfg = ya_payment.Configuration(host="http://127.0.0.1:7465/payment-api/v1")
    api_client = PaymentApiClient(
        configuration=cfg,
        header_name="authorization",
        header_value=f"Bearer {app_key}",
    )
    api = RequestorApi(api_client)
    return api


# create async main
async def main():
    api = prepare_api()

    try:
        allocation = Allocation(
            allocation_id="",
            total_amount="1.3",
            spent_amount="",
            remaining_amount="",
            make_deposit=False,
            payment_platform="erc20-holesky-tglm"
        )
        print(f"Creating allocation: {allocation}")
        allocation1 = await api.create_allocation(allocation)
        print(f"Allocation created: {allocation1}")

        await asyncio.sleep(1)

        allocation_list = await api.get_allocations()
        for allocation in allocation_list:
            if allocation.allocation_id == allocation1.allocation_id:
                print(f"Found allocation match from allocation list: {allocation}")
                break

        await asyncio.sleep(1)

        print(f"Getting allocation: {allocation1.allocation_id}")
        allocation1 = await api.get_allocation(allocation1.allocation_id)
        print(f"Getting allocation: {allocation1.allocation_id} done")

        await asyncio.sleep(1)

        print(f"Releasing allocation: {allocation1.allocation_id}")
        await api.release_allocation(allocation1.allocation_id)
        print(f"Allocation released: {allocation1.allocation_id}")
    finally:
        print("Gracefully disconnecting from the API...")
        await api.api_client.close()
        print("Done")


if __name__ == "__main__":
    asyncio.run(main())