import { chakra, HTMLChakraProps, useColorModeValue } from "@chakra-ui/react";

export const Logo: React.FC<HTMLChakraProps<"svg">> = (props) => {
	const color = useColorModeValue("#231f20", "#fff");
	return (
		<img
			src="static/screenshots/Untitled_Artwork.png"
			alt="logo"
			width="225px"
			height="225px"
			style={{ marginTop: -65 + "px" }}
		/>
	);
};
