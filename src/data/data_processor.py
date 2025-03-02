from llama_index.core import Document

class DataProcessor:
    @staticmethod
    def clean_data(combine_data, injuries_data, rush_data):
        """Clean and prepare the data"""
        combine_data = combine_data.fillna(0)
        injuries_data = injuries_data.fillna('None')
        rush_data = rush_data.fillna(0)
        
        return combine_data, injuries_data, rush_data

    @staticmethod
    def create_documents(combine_data, injuries_data, rush_data):
        """Convert dataframes to documents"""
        def df_to_document(df, description):
            text = f"{description}\n\n"
            for idx, row in df.head(1000).iterrows():
                text += f"Record {idx}:\n"
                for col in df.columns:
                    text += f"{col}: {row[col]}\n"
                text += "\n"
            return Document(text=text)

        documents = [
            df_to_document(combine_data, "NFL Combine Performance Data"),
            df_to_document(injuries_data, "Player Injury History"),
            df_to_document(rush_data, "Rushing Statistics")
        ]
        
        return documents 