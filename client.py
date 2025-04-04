import grpc
import testexecutor_pb2
import testexecutor_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = testexecutor_pb2_grpc.TestExecutorStub(channel)
        while True:
            cmd = input("Enter command to run (or 'exit' to quit): ")
            if cmd.lower() == 'exit':
                break
            response = stub.RunCommand(testexecutor_pb2.CommandRequest(command=cmd))
            print(f"\n Success: {response.success}\n Output:\n{response.output}\n")

if __name__ == "__main__":
    run()
