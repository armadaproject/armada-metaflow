from metaflow import FlowSpec, step, armada


class ArmadaFlow(FlowSpec):
    """A simple flow demonstrating the use of Armada with Metaflow."""

    @step
    def start(self):
        """Sets a local variable."""
        print("Start")
        self.local_var = 214
        print(f"Set self.local_var: {self.local_var}")
        self.next(self.submit_job_decorated)

    @armada(
        host="localhost",
        port="50051",
        logging_host="localhost",
        logging_port="50053",
        queue="test",
        job_set_id="job-set-alpha",
        cpu="240m",
        memory="2Gi",
        insecure_no_ssl=True,
    )
    @step
    def submit_job_decorated(self):
        """Sets a variable within Armada and demonstrates access to data
        from previous steps."""
        print("Hello world from an Armada-launched container!")
        self.armada_var = 1337
        print(f"armada_var: {self.armada_var} local_var: {self.local_var}")
        self.next(self.end)

    @step
    def end(self):
        """Ends the flow and shows that the variable set within Armada is
        available outside."""
        print(f"Armada container variable retrieved outside: {self.armada_var}")
        print(f"local_var: {self.local_var}")
        print("End")


if __name__ == "__main__":
    ArmadaFlow()
