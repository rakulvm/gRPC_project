from concurrent import futures
import grpc
import testexecutor_pb2
import testexecutor_pb2_grpc
import subprocess

class TestExecutorServicer(testexecutor_pb2_grpc.TestExecutorServicer):
    def RunCommand(self, request, context):
        try:
            result = subprocess.run(request.command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
            output = result.stdout if result.stdout else result.stderr
            return testexecutor_pb2.CommandResponse(success=True, output=output)
        except Exception as e:
            return testexecutor_pb2.CommandResponse(success=False, output=str(e))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    testexecutor_pb2_grpc.add_TestExecutorServicer_to_server(TestExecutorServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
