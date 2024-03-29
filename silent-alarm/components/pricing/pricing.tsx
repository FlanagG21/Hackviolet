import {
	Box,
	Heading,
	HStack,
	Icon,
	SimpleGrid,
	StackProps,
	Text,
	VStack,
} from "@chakra-ui/react";
import {
	ButtonLink,
	ButtonLinkProps,
} from "components/button-link/button-link";
import { BackgroundGradient } from "components/gradients/background-gradient";
import { Section, SectionProps, SectionTitle } from "components/section";
import React from "react";
import { FiCheck } from "react-icons/fi";

export interface PricingPlan {
	id: string;
	title: React.ReactNode;
	description: React.ReactNode;
	price: React.ReactNode;
	features: Array<PricingFeatureProps | null>;
	action: ButtonLinkProps & { label?: string };
	isRecommended?: boolean;
}

export interface PricingProps extends SectionProps {
	description: React.ReactNode;
	plans: Array<PricingPlan>;
}

const PricingFeatures: React.FC<React.PropsWithChildren<{}>> = ({
	children,
}) => {
	return (
		<VStack
			align="stretch"
			justifyContent="stretch"
			spacing="4"
			mb="8"
			flex="1"
		>
			{children}
		</VStack>
	);
};

export interface PricingFeatureProps {
	title: React.ReactNode;
	iconColor?: string;
}

const PricingFeature: React.FC<PricingFeatureProps> = (props) => {
	const { title, iconColor = "primary.500" } = props;
	return (
		<HStack>
			<Icon as={FiCheck} color={iconColor} />
			<Text flex="1" fontSize="sm">
				{title}
			</Text>
		</HStack>
	);
};

export interface PricingBoxProps extends Omit<StackProps, "title"> {
	title: React.ReactNode;
	description: React.ReactNode;
	price: React.ReactNode;
}

const PricingBox: React.FC<PricingBoxProps> = (props) => {
	const { title, description, price, children, ...rest } = props;
	return (
		<VStack
			zIndex="2"
			bg="whiteAlpha.600"
			borderRadius="md"
			p="8"
			flex="1 0"
			alignItems="stretch"
			border="1px solid"
			borderColor="gray.400"
			_dark={{
				bg: "blackAlpha.300",
				borderColor: "gray.800",
			}}
			{...rest}
		>
			<Heading as="h3" size="md" fontWeight="bold" fontSize="lg" mb="2">
				{title}
			</Heading>
			<Box color="muted">{description}</Box>
			<Box fontSize="2xl" fontWeight="bold" py="4">
				{price}
			</Box>
			<VStack
				align="stretch"
				justifyContent="stretch"
				spacing="4"
				flex="1"
			>
				{children}
			</VStack>
		</VStack>
	);
};
