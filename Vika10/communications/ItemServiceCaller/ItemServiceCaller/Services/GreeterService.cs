using Grpc.Core;
using ItemServiceCaller;

namespace ItemServiceCaller.Services;

public class GreeterService(ILogger<GreeterService> logger, openapiClient client) : Greeter.GreeterBase
{
    private readonly ILogger<GreeterService> _logger = logger;

    public override async Task<HelloReply> SayHello(HelloRequest request, ServerCallContext context)
    {
        var item = await client.PostAsync(new ItemCreateRequest
        {
            Name = request.Name,
            Email = "test@email.com"
        });

        return new HelloReply
        {
            Message = "Hello " + item.Id
        };
    }
}
