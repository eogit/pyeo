import pyeo.classification
import pyeo.filesystem_utilities
import configparser
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Produces a trained model from a folder containing '
                                                 'rasters and shapefiles')
    parser.add_argument("region_path", type=str, action='store',
                        help="Path to the folder containing the region data")
    parser.add_argument("training_class", type=str, action='store',
                        help="Attribute field holding the class to train on")
    parser.add_argument("out_path", type=str, action="store",
                        help="Path for the output .pkl file")
    args = parser.parse_args()

    conf = configparser.ConfigParser()

    log = pyeo.filesystem_utilities.init_log("model.log")

    log.info("***MODEL CREATION START***")

    pyeo.classification.create_model_for_region(args.region_path, args.out_path,
                                                args.training_class.rsplit('.')[0] +"_scores.txt",
                                                args.training_class)

    log.info("***MODEL CREATION END***")
