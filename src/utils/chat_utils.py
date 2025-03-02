class ChatHistory:
    @staticmethod
    def format_response(response):
        """Format the agent's response for better display"""
        # Remove any system-level messages or debug info
        if isinstance(response, str):
            # Clean up the response
            response = response.replace('Assistant:', '')
            response = response.replace('Human:', '')
            response = response.strip()
            
            # Add markdown formatting
            response = f"""
            {response}
            
            ---
            """
            
        return response 