import pandas as pd
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq


class database:
    def __init__(self, variants, af):
        # variants df, af list of np1d in order of columns in variants df
        self.variants = variants
        self.af = af
    # sample is input_variants df

    def add_sample(self, sample):
        # step 0: remove af column and append to af list of np1d arrays
        self.af.append(sample.pop('AF'))
        # step 1: add columns of every sample in database filled with 0s, input sample filled with 1s
        # get variant database column names as list, excluding pos ref alt (those are not sample names)
        variant_columns = list(self.variants.columns)[3:]
        # create 0s with other samples columns
        zero_cols_matrix_dimensions = (len(sample.index), len(variant_columns))
        database_zero_cols = pd.DataFrame(data=np.zeros(zero_cols_matrix_dimensions), columns=variant_columns)
        sample = pd.concat([sample, database_zero_cols], axis=1)
        revised_input = sample.assign(D=1)
        copy_df = pd.concat([self.variants, sample])
        # print(self.variants.merge(sample, how='inner', on=['POS', 'REF', 'ALT']).iloc[:, :-len(variant_columns)])
        
        print(revised_input)
        print(copy_df)
        return None


database_variants = pd.DataFrame(columns=['POS', 'REF', 'ALT', 'A', 'B', 'C'],
                                 data=[['15', 'C', 'G', 1, 0, 0],
                                       ['17', 'C', 'G', 0, 1, 0],
                                       ['18', 'C', 'G', 0, 0, 1]])

database_af = [np.array([.13]), np.array([.17]), np.array([.18])]

# input variants includes the allele frequency of the sample, filename is the column name ie A.csv
input_variants = pd.DataFrame(columns=['POS', 'REF', 'ALT', 'AF'],
                              data=[['17', 'C', 'G', .19],
                                    ['16', 'C', 'G', .18]])

test_db = database(database_variants, database_af)
test_db.add_sample(input_variants)
