import requests
import threading

# الدالة التي تقوم بإرسال الطلبات المتعددة
def send_request(url):
    try:
        response = requests.get(url)
        print(f"Request to {url} - Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending a request to {url}: {str(e)}")

# الدالة الرئيسية لتشغيل السكريبت
def main():
    url = input("Enter the target URL: ")
    num_requests = int(input("Enter the number of requests to send: "))

    print(f"Sending {num_requests} requests to {url}...\n")

    # قم بإنشاء مجموعة من الخيوط لإرسال الطلبات المتعددة
    threads = []
    for _ in range(num_requests):
        t = threading.Thread(target=send_request, args=(url,))
        threads.append(t)
        t.start()

    # انتظر انتهاء جميع الخيوط
    for t in threads:
        t.join()

    print("\nAll requests have been sent.")

# تشغيل السكريبت عند تشغيله كبرنامج مستقل
if __name__ == '__main__':
    main()

